from django.urls import path

from . import views

app_name = 'orm_abc_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('datetime_nov/', views.datetime_nov, name='datetime_nov'),
    path('var_list_dict/', views.var_list_dict, name='var_list_dict'),
    path('task_form/', views.task_form, name='task_form'),
    path('task_get/', views.task_get, name='abc_get'),
    path('form_create_0/', views.form_create_0, name='form_create_0'),
    path('form_create/', views.form_create, name='form_create'),
    path('task_result/', views.task_result, name='task_result'),
    path('table/', views.table, name='table'),
]
