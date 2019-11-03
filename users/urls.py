# api/urls.py
from django.urls import path, include

from . import views

urlpatterns = [
    path('list/', views.UserListView.as_view()),
    path('user/<int:pk>/', views.UserProfile.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
