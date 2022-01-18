from django.urls import path
from . import views


urlpatterns = [
    path('', views.dress_list, name='dress_list'),
]
