from django.urls import path
from . import views

urlpatterns = [
    path('', views.automation_list, name='automation_list'),
    path('create/', views.automation_create, name='automation_create'),
    path('update/<int:pk>/', views.automation_update, name='automation_update'),
    path('delete/<int:pk>/', views.automation_delete, name='automation_delete'),
]
