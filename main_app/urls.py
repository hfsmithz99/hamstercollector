from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('hamsters/', views.hamsters_index, name='index'),
    path('hamsters/<int:hamster_id>/', views.hamster_detail, name="detail"),
]