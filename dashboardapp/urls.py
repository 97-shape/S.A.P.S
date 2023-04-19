from django.urls import path, include
from dashboardapp import views

app_name = "dashboardapp"

urlpatterns = [
    # path('list/', views.ShowData, name='list'),
    path('main/', views.Dashboard_display, name='main'),
    path('chart/<str:device_id>', views.DisplayData, name='chart'),
    path('notice', views.NoticeList, name='notice'),
    path('FAQ', views.FAQList, name='FAQ'),
    path('write/<str:board_type>/', views.BoardWrite, name='write'),
    path('content/<str:board_type>/<int:board_id>/', views.BoardContent, name='content'),
    path('edit/<int:board_id>/', views.BoardEdit, name='edit'),
    path('delete/<str:board_type>/<int:board_id>/', views.BoardDelete, name='delete')
]