from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, SpecimenViewSet, SourceDescriptionViewSet, PatientViewSet, LocationViewSet, OtherDetailsViewSet, RecordViewSet

# Create a router and register the OrderViewSet
router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'specimens', SpecimenViewSet)
router.register(r'source-descriptions', SourceDescriptionViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'otherdetails', OtherDetailsViewSet)
router.register(r'record', RecordViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
]
