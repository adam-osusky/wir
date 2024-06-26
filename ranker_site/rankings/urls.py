from django.urls import path, include
from . import views

urlpatterns = [
    path('task/', views.task_detail, name='task_detail'),
    path('submit_task', views.submit_task, name='submit_task'),
    path('score_task/', views.score_task, name='score_task'),
    path('leaderboard', views.user_leaderboard, name='user_leaderboard'),
    # path('score/<int:pk>/', views.score_page, name='score'),
    # path('save_word_order/', views.save_word_order, name='save_word_order'),
]
