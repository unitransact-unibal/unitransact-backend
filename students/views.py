from rest_framework import viewsets, permissions

from .models import Student
from .serializer import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
