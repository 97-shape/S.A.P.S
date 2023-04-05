from django.urls import path

from dashboardapp import views

app_name = "dashboardapp"

urlpatterns = [
    path('list/', views.ShowData, name='list'),
]