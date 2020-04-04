from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:car_id>/', views.detail, name='detail'),
    path('<int:car_id>/add_comment/', views.add_comment, name='add_comment'),
    path('<int:car_id>/delete_car/', views.delete_car, name='delete_car'),
    path('<slug:slug>/', views.ProfileDetail.as_view(), name='profile-detail'),
    path('personalCabinet', views.personalCabinet, name='personalCabinet'),
]
