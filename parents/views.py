from rest_framework import viewsets, permissions, filters
from filters.mixins import (
    FiltersMixin,
)

from .models import Parent
from .serializer import ParentSerializer


class ParentViewSet(FiltersMixin, viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    lookup_field = "user_id"

    filter_backends = (filters.OrderingFilter,)
    filter_mappings = {
        'id': 'id'
    }
