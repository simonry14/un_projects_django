from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add, name="add"),
    path('view/<str:id>/', views.view , name="view"),
    path('edit/<str:id>/', views.edit, name="edit")
]

urlpatterns += staticfiles_urlpatterns()

