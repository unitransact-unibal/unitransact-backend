from django.db import models
from django.contrib.auth import get_user_model


class DonationsWalletTransactions(models.Model):
    DEBIT = 'db'
    CREDIT = 'cr'
    TYPE_CHOICES = [
        (DEBIT, 'debit'),
        (CREDIT, 'credit'),
    ]

    user_id = models.OneToOneField(
        get_user_model(), on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    transaction_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default=DEBIT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'donations_wallet_transactions'
