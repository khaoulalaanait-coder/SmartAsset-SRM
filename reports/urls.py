from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReportViewSet, PhotoViewSet, ReportHistoryViewSet

router = DefaultRouter()
router.register(r'reports', ReportViewSet, basename='report')
router.register(r'photos', PhotoViewSet, basename='photo')
router.register(r'history', ReportHistoryViewSet, basename='reporthistory')

urlpatterns = [
    path('', include(router.urls)),
]
