from rest_framework import viewsets, permissions

from .models import Student, StudentParent, StudentWalletTransaction
from .serializer import StudentParentSerializer, StudentSerializer, StudentWalletTransactionSerializer


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentParentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = StudentParent.objects.all()
    serializer_class = StudentParentSerializer


class StudentWalletTransactionViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = StudentWalletTransaction.objects.all()
    serializer_class = StudentWalletTransactionSerializer
