from rest_framework import viewsets, permissions

from .models import Parent
from .serializer import ParentSerializer


class ParentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    lookup_field = "user_id"
