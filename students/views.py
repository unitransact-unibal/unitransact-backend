from rest_framework import viewsets, permissions

from students.models import Student
from students.serializer import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
