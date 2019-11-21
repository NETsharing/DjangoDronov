
# from django.contrib import admin
from django.urls import path
from .views import index, by_rubric, BbCreateView, add, add_save
# app_name = 'bboard'
urlpatterns = [
path ('<int:rubric_id>/', by_rubric, name='by_rubric'),
path ('', index, name='index'),
path ('add/', BbCreateView.as_view(), name='add'),
path ('add/ save/ ', add_save, name='add_save'),
path ('add/', add, name='add'),

]
