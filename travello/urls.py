from django.urls import path

from . import views

#urlpatterns = [
#    path('', views.index, 'index'),
#]

urlpatterns = [
    path('', views.index, name='index'),
    #path('name', views.name, name='name'),
    #path('add', views.add, name="add"),
    #path('do_addition', views.do_addition, name='do_addition'),
]

