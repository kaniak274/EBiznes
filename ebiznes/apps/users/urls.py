from django.urls import path

from . import views


urlpatterns = [
    path('', views.base_view),
    path('login/', views.base_view),
    path('register/', views.base_view),
    path('services/', views.base_view),
]
