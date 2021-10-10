from rest_framework import serializers
from .models import Student, Parent


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
            'school_id',
            'user_id',
            'created_at',
            'updated_at',
        )


class StudentParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = (
            'student_id',
            'parent_id',
            'created_at',
            'updated_at',
        )
