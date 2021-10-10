from rest_framework import serializers
from .models import Parent


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = (
            'id',
            'national_id',
            'first_name',
            'last_name',
            'telephone',
            'address',
            'country',
            'user_id',
            'created_at',
            'updated_at',
        )
