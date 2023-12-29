from django.urls import path, include
from rest_framework import routers
from webhooks.views import CaseViewSet

router = routers.DefaultRouter()
router.register(r'cases', CaseViewSet, basename='cases')

urlpatterns = [
    path('', include(router.urls)),
]
