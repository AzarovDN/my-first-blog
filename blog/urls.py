from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    url(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.PostCreateView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostEditView.as_view(), name='post_edit'),

]
