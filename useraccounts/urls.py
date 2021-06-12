from django.urls import path

from . import views

HOMEPAGE = '/'
REGISTER_PAGE = 'register'
LOGIN_PAGE = 'login'

REGISTER_ACTION = 'add_user'
LOGIN_ACTION = 'do_login'
LOGOUT_ACTION = 'do_logout'

urlpatterns = [
    path(REGISTER_PAGE, views.register, name='register'),
    path(REGISTER_ACTION, views.add_new_user, name = 'add_new_user'),
    path(LOGIN_PAGE, views.login, name = "login"),
    path(LOGIN_ACTION, views.do_login, name = 'do_login'),
    path(LOGOUT_ACTION, views.do_logout, name = 'do_logout'),
    #path('name', views.name, name='name'),
    #path('add', views.add, name="add"),
    #path('do_addition', views.do_addition, name='do_addition'),
]
