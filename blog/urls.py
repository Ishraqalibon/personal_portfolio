from django.contrib import admin
from django.urls import path ,include
from blog import  views
app_name='project'
urlpatterns = [

    path('',views.blog,name='all_blogs'),
    path('<int:blog_id>/',views.detail,name='detail'),


]