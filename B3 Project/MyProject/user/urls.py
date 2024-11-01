from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index),
    path('home/',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('gallery/',views.gallery),
    path('video/',views.video),
    path('blog/',views.blog),
    path('donate/',views.donate),
    path('membership/',views.membership),
    path('',views.index),
 #   path('login/',views.login),
    path('causes/',views.causes),
    path('details/',views.vdodetails),
    path('bdetail/',views.blogdetail),


]

