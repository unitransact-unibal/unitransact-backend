from rest_framework import viewsets, permissions, filters
from filters.mixins import (
    FiltersMixin,
)

from .models import Student, StudentParent, StudentWalletTransaction
from .serializer import StudentParentSerializer, StudentSerializer, StudentWalletTransactionSerializer


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "user_id"


class StudentParentViewSet(FiltersMixin, viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = StudentParent.objects.all()
    serializer_class = StudentParentSerializer
    filter_backends = (filters.OrderingFilter,)
    filter_mappings = {
        'student_id': 'student_id',
        'parent_id': 'parent_id',
    }


class StudentWalletTransactionViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = StudentWalletTransaction.objects.all()
    serializer_class = StudentWalletTransactionSerializer
