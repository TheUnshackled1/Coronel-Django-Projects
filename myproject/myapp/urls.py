from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('about/', views.about, name='about'),
    path("menu/", views.menu, name="menu"),
    path("contact/", views.contact, name="contact"),
    path('news/', views.news, name='news'),
    path("story/", views.story, name='story'),
    path('calcu/', views.calcu, name='calcu')
]


