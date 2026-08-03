from rest_framework import serializers
from .models import Report, Photo, ReportHistory

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image', 'type', 'uploaded_at']  # ✅ 'image' f blasset 'image_url'


class ReportHistorySerializer(serializers.ModelSerializer):
    changed_by_username = serializers.ReadOnlyField(source='changed_by.username')

    class Meta:
        model = ReportHistory
        fields = ['id', 'old_status', 'new_status', 'changed_by', 'changed_by_username', 'changed_at']


class ReportSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    history = ReportHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Report
        fields = [
            'id', 'equipment', 'anomaly_type', 'description', 
            'latitude', 'longitude', 'priority', 'status', 
            'duplicate_counter', 'photos', 'history', 
            'created_at', 'updated_at'
        ]