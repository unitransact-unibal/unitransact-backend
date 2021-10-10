from rest_framework import serializers
from .models import School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = (
            'id',
            'name',
            'address',
            'location',
            'user_id',
            'created_at',
            'updated_at',
        )
