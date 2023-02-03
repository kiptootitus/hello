from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('myapp/', views.members, name='myapp'),
    path('myapp/details/<int:id>/', views.details, name='details'),
]