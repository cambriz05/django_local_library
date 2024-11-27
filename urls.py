from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("quiz/", views.quiz_view, name="quiz"),
]