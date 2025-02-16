from django.urls import path,include
from .views import PatientViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('paitent', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
