from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/delete', views.post_delete, name='post_delete'),
    path('post/<int:post_id>', views.post_detail, name='post_detail'),
    # path('post/new', views.post_create, name='post_create'),
    # path('post/<int:id>/edit', views.post_edit, name='post_edit'),
    # path('search/', views.post_search, name='post_search'),
]