from django.urls import path, include
from . import views

urlpatterns = [
    # path('task<int:pk>/', views.task_detail, name='task_detail'),
    path('task<int:pk>/', views.task_detail, name='task_detail'),
]
