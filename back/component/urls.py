from django.urls import path

from . import views

urlpatterns = [
    path('', views.ComponentView.as_view()),
    # path('<int:id><str:word>/', views.ComponentNameView.as_view()),
]