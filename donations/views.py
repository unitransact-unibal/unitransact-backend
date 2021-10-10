from rest_framework import viewsets, permissions

from donations.models import DonationsWalletTransaction
from donations.serializer import DonationsWalletTransactionSerializer


class DonationsWalletTransactionViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = DonationsWalletTransaction.objects.all()
    serializer_class = DonationsWalletTransactionSerializer
