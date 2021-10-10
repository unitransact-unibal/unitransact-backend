from rest_framework import generics, permissions

from students.models import Student
from students.serializer import StudentSerializer


class ListStudent(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
