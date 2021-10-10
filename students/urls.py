from rest_framework.routers import SimpleRouter

from .views import StudentParentViewSet, StudentViewSet, StudentWalletTransactionViewSet

router = SimpleRouter()
router.register('', StudentViewSet, basename="students")
router.register(
    'parents', StudentParentViewSet,
    basename="students.parents"
)
router.register(
    'wallets/transactions', StudentWalletTransactionViewSet,
    basename="students.transactions.wallets"
)

urlpatterns = router.urls
