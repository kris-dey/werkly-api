# api/urls.py
from django.urls import path, include

from . import views

urlpatterns = [
    path('list/', views.JobListView.as_view()),
    path('create/', views.CreateJobView.as_view()),
    path('rightSwipe/<int:pk>/', views.RightSwipe.as_view(), name='update_right_swipes'),
]
