from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    path('', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # path('post/(?P<pk>\d+)/', views.post_detail, name='post_detail'),

]
