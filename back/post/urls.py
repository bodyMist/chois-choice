from django.urls import path, include
from . import views

urlpatterns = [
    # FBV
    path('post/', views.PostListAPIView.as_view()),
    path('post/<int:pk>/',views.PostDetailAPIView.as_view()),
]