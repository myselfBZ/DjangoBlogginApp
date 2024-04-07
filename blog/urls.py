from django.urls import path 
from . import views

urlpatterns = [
    path('posts/', views.blogs, name='posts'),
    path('post/<int:pk>', views.blog, name='post'),
    path('create-post/', views.create_blog, name='create-post'),
    path('update/<int:pk>', views.update_post, name='update-post'),
    path('delete-post/<int:pk>', views.delete_post, name='delete-post'),
    path('comment/<int:pk>', views.write_comment, name='comment')
]