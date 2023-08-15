from rest_framework.routers import DefaultRouter
from .views import ContactModelViewSet, ContactNumberModelViewSet

router = DefaultRouter()

router.register('contacts', ContactModelViewSet, basename='contacts')
router.register('numbers', ContactNumberModelViewSet, basename='numbers')

urlpatterns = router.urls
