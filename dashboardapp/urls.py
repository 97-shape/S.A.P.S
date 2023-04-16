from django.urls import path

from dashboardapp import views

app_name = "dashboardapp"

urlpatterns = [
    # path('list/', views.ShowData, name='list'),
    path('main/', views.Dashboard_display, name='main'),
    path('chart/<str:device_id>', views.DisplayData, name='chart'),
    path('notice', views.BoardList, name='notice'),
    path('write', views.BoardWrite, name='write'),
]