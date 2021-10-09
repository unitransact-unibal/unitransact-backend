from django.db.models import query
from rest_framework import generics

from students.models import Student
from students.serializer import StudentSerializer


class ListStudent(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DetailStudent(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
