from rest_framework.routers import SimpleRouter

from .views import DonationsWalletTransactionViewSet

router = SimpleRouter()
router.register(
    'wallets/transactions', DonationsWalletTransactionViewSet,
    basename="donations.wallets.transactions"
)

urlpatterns = router.urls
