from announcement_app.models import Announcement
from rest_framework import serializers
from user_app.serializers import UserSerializer

class AnnouncementSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    approved_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Announcement
        fields = ['id', 'title','content','created_by','created_at','expiration_date','status','approved_by','approved_at']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['created_at'] = instance.created_at.strftime('%d-%m-%Y %H:%M:%S')
        representation['approved_at'] = instance.approved_at.strftime('%d-%m-%Y %H:%M:%S') if instance.approved_at else None

        return representation