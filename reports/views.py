from rest_framework import viewsets, permissions
from .models import Report, Photo, ReportHistory
from .serializers import ReportSerializer, PhotoSerializer, ReportHistorySerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.AllowAny]

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.AllowAny]

class ReportHistoryViewSet(viewsets.ModelViewSet):
    queryset = ReportHistory.objects.all()
    serializer_class = ReportHistorySerializer
    permission_classes = [permissions.AllowAny]