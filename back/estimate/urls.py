from django.urls import path

from . import views

urlpatterns = [
  path('', views.Recommendation.as_view()),
]