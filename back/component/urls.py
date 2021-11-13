from django.urls import path

from . import views

urlpatterns = [
    path('', views.ComponentView.as_view()),
    path('/cpu/list',views.CpuListView.as_view()),
    path('/gpu/list',views.GpuListView.as_view()),
    path('/mainboard/list', views.MainboardListView.as_view()),
    path('/memory/list',views.MemoryListView.as_view()),
    path('/hdd/list', views.HddListView.as_view()),
    path('/ssd/list', views.SsdListView.as_view()),
    path('/power/list',views.PowerListView.as_view()),
    path('/cooler/list',views.CoolerListView.as_view()),
    path('/case/list', views.CaseListView.as_view()),

    path('/cpu/detail', views.CpuDetailView.as_view()),
    path('/gpu/detail', views.GpuDetailView.as_view()),
    path('/mainboard/detail', views.MainboardDetailView.as_view()),
    path('/memory/detail', views.MemoryDetailView.as_view()),
    path('/hdd/detail', views.HddDetailView.as_view()),
    path('/ssd/detail', views.SsdDetailView.as_view()),
    path('/power/detail', views.PowerDetailView.as_view()),
    path('/cooler/detail', views.CoolerDetailView.as_view()),
    path('/case/detail/', views.CaseDetailView.as_view()),
]