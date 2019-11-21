from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'services', views.ServiceViewset, base_name='services')

urlpatterns = [
    path('professions/', views.ProfessionListView.as_view(), name='professions'),
    path('ratings/', views.CreateRatingAPIView.as_view(), name='ratings'),
    path('ratings/<int:pk>/', views.UpdateRating.as_view(), name='ratings-update'),
    path('check-rating/<int:pk>/', views.CheckRatingAPIView.as_view(), name='check-rating'),
    path('rents/', views.RentListAPIView.as_view(), name='rents'),
    path('price-list/', views.CreatePriceListRecord.as_view(), name='price-list'),
    path('price-list/remove/<int:pk>/', views.RemovePriceListRecord.as_view(), name='remove-price-list'),
    path('price-list/update/<int:pk>/', views.UpdatePriceListRecord.as_view(), name='update-price-list'),
] + router.urls
