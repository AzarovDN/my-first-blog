from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='post_edit'),

]
