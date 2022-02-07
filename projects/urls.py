from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutPage, name="logout"),
    path('register', views.registerPage, name="register"),
    path('', views.home, name="home"),
    path('add/', views.add, name="add"),
    path('view/<str:id>/', views.view , name="view"),
    path('edit/<str:id>/', views.edit, name="edit"),
     path('delete/<str:id>/', views.delete, name="delete")
]

urlpatterns += staticfiles_urlpatterns()

