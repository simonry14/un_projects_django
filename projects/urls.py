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
    path('delete/<str:id>/', views.delete, name="delete"),
    path('all/', views.all, name="all"),
    path('country/<countr>', views.by_country, name="by_country"),
    path('Approval Status/<statu>', views.by_status, name="by_approval")
]

urlpatterns += staticfiles_urlpatterns()

