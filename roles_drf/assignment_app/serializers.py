from assignment_app.models import Answer, Assignment
from rest_framework import serializers
from user_app.serializers import UserSerializer

class AssignmentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Assignment
        fields = ['id', 'title','description','created_by','created_at','due_date']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at.strftime('%d-%m-%Y %H:%M:%S')
        return representation

class AnswerSerializer(serializers.ModelSerializer):

    created_by = UserSerializer(read_only=True)
    evaluvated_by = UserSerializer(read_only=True)
    # assignment = AssignmentSerializer(read_only=True)
    
    class Meta:
        model = Answer
        fields = ['id', 'assignment','answer_text','created_by','created_at','marks','evaluvated_by','evaluvated_at', 'remarks']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at.strftime('%d-%m-%Y %H:%M:%S')
        representation['evaluvated_at'] = instance.created_at.strftime('%d-%m-%Y %H:%M:%S')
        return representation