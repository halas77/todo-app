from django.contrib import admin
from django.urls import path
from .views import home, remove


urlpatterns = [
    path('', home, name='todo'),
    path('del/<str:item_id>', remove, name='del')
]




  