from django.urls import path
from . import views


app_name ='blog'

urlpatterns=[
path("",views.index,name='index'),
path("about/",views.about,name='about'),
path("twitter/",views.tweet,name='tweet'),
path("<int:blog_id>/",views.detail,name='detail'),
path("<int:blog_id>/comment/",views.comment,name='comment'),
path("<int:blog_id>/ack/",views.ack,name='ack'),
]
