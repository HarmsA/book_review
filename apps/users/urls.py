from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^index/$', views.user_index, name='user_index'),
    url(r'^kill/$', views.kill, name='kill'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^verify_login/$', views.verify_login, name='verify_login'),
    url(r'^verify_register/$', views.verify_register, name='verify_register'),
]
