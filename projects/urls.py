from django.urls import path, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutPage, name="logout"),
    path('register', views.registerPage, name="register"),
    path('', views.home, name="home"),
    path('add/', views.add, name="add"),
    path('projects/view/<str:id>/', views.view , name="view"),
    path('projects/edit/<str:id>/', views.edit, name="edit"),
    path('projects/delete/<str:id>/', views.delete, name="delete"),
    path('get_all/', views.get_all, name="all"),
    path('get_by_country/<countr>', views.get_by_country, name="by_country"),
    path('get_by_status/<statu>', views.get_by_status, name="by_approval"),
    path('add_project/', views.add_project, name="add_project"),
    path('delete_project/<str:id>/', views.delete_project, name="delete_project"),
    path('dashboard/', views.dashboard, name="dashboard"),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += staticfiles_urlpatterns()

