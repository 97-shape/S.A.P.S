from django.urls import path

from dashboardapp import views

app_name = "dashboardapp"

urlpatterns = [
    path('list/', views.ShowData, name='list'),
    path('main/', views.dashboard_display, name='main'),
    path('chart/', views.ShowChart, name='chart'),
]