from rest_framework import serializers
from .models import Parent


class ParentSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source='user_id.first_name')
    last_name = serializers.ReadOnlyField(source='user_id.last_name')

    class Meta:
        model = Parent
        fields = (
            'id',
            'national_id',
            'telephone',
            'address',
            'country',
            'user_id',
            'first_name',
            'last_name',
            'created_at',
            'updated_at',
        )
