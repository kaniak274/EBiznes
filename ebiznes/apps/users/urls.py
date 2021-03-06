from django.urls import path

from . import views

from ebiznes.apps.service.views import payment_view

urlpatterns = [
    path('', views.base_view),
    path('login', views.base_view),
    path('register', views.base_view),
    path('services/', views.base_view),
    path('services/your-services', views.base_view),
    path('services/create', views.base_view),
    path('services/detail/<int:id>', views.base_view_id),
    path('services/edit/<int:id>', views.base_view_id),
    path('password-change/', views.base_view),
    path('your-account/', views.base_view),
    path('privacy/', views.base_view),
    path('rent-history/', views.base_view),
    path('about/', views.base_view),
    path('contact/', views.base_view),
    path('rules/', views.base_view),
    path('payment/rent/<int:pk>/', payment_view, name='payment'),
]
