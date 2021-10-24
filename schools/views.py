from rest_framework import viewsets, permissions, filters
from filters.mixins import (
    FiltersMixin,
)

from .models import School
from .serializer import SchoolSerializer


class SchoolViewSet(FiltersMixin ,viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    lookup_field = "user_id"

    filter_backends = (filters.OrderingFilter,)
    filter_mappings = {
        'user_id': 'user_id',
    }
