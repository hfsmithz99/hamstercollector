from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('hamsters/', views.hamsters_index, name='index'),
    path('hamsters/<int:hamster_id>/', views.hamster_detail, name="detail"),
    path('hamsters/create', views.HamsterCreate.as_view() ,name='hamsters_create'),
    path('hamsters/<int:pk>/update/', views.HamsterUpdate.as_view(), name='hamsters_update'),
    path('hamsters/<int:pk>/delete/', views.HamsterDelete.as_view(), name='hamsters_delete'),
    path('hamsters/<int:hamster_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyCreate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('hamsters/<int:hamster_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name="assoc_toy"),
]