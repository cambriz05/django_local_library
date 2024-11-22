from django.urls import path
from . import views

urlpatterns = [
   path('user_profile/', views.user_profile_view, name='user_profile'),
   path('leaderboard/', views.leaderboard_view, name="leaderboard"),
   path('dashboard/', views.dashboard_view, name="dashboard"),
]