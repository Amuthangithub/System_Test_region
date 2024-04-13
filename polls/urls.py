from . import views
from django.urls import path
urlpatterns = [
    path("", views.hello,name="empty"),
    path("index", views.index, name="index"),
    path("random", views.random, name="random")
    
]