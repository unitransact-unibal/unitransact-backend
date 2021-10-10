from rest_framework import serializers
from .models import DonationsWalletTransaction


class DonationsWalletTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationsWalletTransaction
        fields = (
            'id',
            'user_id',
            'amount',
            'transaction_type',
            'created_at',
            'updated_at',
        )
