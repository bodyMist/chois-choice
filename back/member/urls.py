from django.urls import path
from . import views

urlpatterns = [
    # path('', views.MemberView.as_view({'get': 'list'})),
    # path('<int:pk>/', views.DetailMember.as_view()),
    path('signup', views.SignUp),
    path('mypage', views.MemberDetail.as_view()),
]