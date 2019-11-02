from django.urls import path

from . import views


urlpatterns = [
    path('', views.base_view),
    path('login', views.base_view),
    path('register', views.base_view),
    path('services/', views.base_view),
    path('services/your-services', views.base_view),
    path('services/create', views.base_view),
    path('services/detail/<int:id>', views.base_view_id),
    path('services/edit/<int:id>', views.base_view_id),
]
