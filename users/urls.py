from django.urls import path 
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('profile/<str:username>', views.see_profile, name='profile'),
    path('profile-update/', views.update_profile, name='update-profile')
]

