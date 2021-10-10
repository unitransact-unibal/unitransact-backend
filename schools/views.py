from rest_framework import viewsets, permissions

from .models import School
from .serializer import SchoolSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
