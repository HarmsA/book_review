from django.db import models
import bcrypt

class UserManager(models.Manager):
    def v_login(self, form):
        errors = []
        try:
            user = self.get(username=form['username'])
            if not bcrypt.checkpw(form['password'].encode(), user.password.encode()):
                errors.append('Username or password is incorrect.')
                return errors
        except:
            errors.append('Username or password is incorrect.')
            return errors
        return errors

    def v_register(self, form):
        errors = []
        username_list = []
        try:
            username_list = self.filter(username=form['username'])
        except:
            if len(username_list)>0:
                errors.append('Username already taken.')
        if len(form['username'])<2:
            errors.append('Username must be longer than 1 letter.')
        if len(form['f_name']) < 2:
            errors.append('First Name must be at least 2 characters long.')
        if len(form['l_name']) < 2:
            errors.append('Last Name must be at least 2 characters long.')
        if len(form['password']) < 2:
            errors.append('Password is to short.')
        if form['password'] != form['confirm_password']:
            errors.append('Password must match the Confirm password')
        return errors

    def create_user(self, form):
        pw_hash = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt())

        user = self.create(
            f_name=form['f_name'],
            l_name=form['l_name'],
            username=form['username'],
            password=pw_hash,
        )
        return user


class User(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
