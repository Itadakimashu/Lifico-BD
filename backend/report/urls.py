from django.urls import path,include
from .views import SymtomViewSet, ReportViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('symtom', SymtomViewSet)
router.register('reportsymtom', ReportViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
