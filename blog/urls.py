from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='posts'),
    # path('post/<int:num>/', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
    # path('post/(?P<pk>\d+)/', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.PostCreateView.as_view(), name='post_new'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostEditView.as_view(), name='post_edit'),
    # url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

]
