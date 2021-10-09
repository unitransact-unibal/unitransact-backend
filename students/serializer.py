from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'id',
            'admission_number',
            'school_id',
            'address',
            'date_of_birth',
            'telephone',
            'country',
            'first_name',
            'last_name',
            'school_id',
            'created_at',
            'updated_at',
        )
