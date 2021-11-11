from rest_framework import serializers
from .models import Student, StudentParent, StudentWalletTransaction


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
