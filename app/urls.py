from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('fort/<str:fort_name>',views.fort,name='fort'),
    path('contact/',views.contactUs,name="contact_us"),
    path('signup',views.signup,name="signup"),
    path('login/',views.userLogin,name="login"),
    path("logout/",views.userLogout,name="logout"),
    path('about/',views.about,name="about"),
]