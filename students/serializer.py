from rest_framework import serializers

from parents.serializer import ParentSerializer
from .models import Student, StudentParent, StudentWalletTransaction


class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source='user_id.first_name')
    last_name = serializers.ReadOnlyField(source='user_id.last_name')

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
            'first_name',
            'last_name',
            'created_at',
            'updated_at',
        )


class StudentParentSerializer(serializers.ModelSerializer):
    parent_id = ParentSerializer(many=False)
    student_id = StudentSerializer(many=False)

    class Meta:
        model = StudentParent
        fields = (
            'id',
            'student_id',
            'parent_id',
            'created_at',
            'updated_at',
        )


class StudentWalletTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentWalletTransaction
        fields = (
            'id',
            'user_id',
            'student_id',
            'amount',
            'transaction_type',
            'created_at',
            'updated_at',
        )
