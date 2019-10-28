from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'services', views.ServiceViewset, base_name='services')

urlpatterns = [] + router.urls
