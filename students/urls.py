from rest_framework.routers import SimpleRouter

from .views import StudentParentViewSet, StudentViewSet, StudentWalletTransactionViewSet

router = SimpleRouter()
router.register(
    'parents', StudentParentViewSet,
    basename="students.parents"
)
router.register(
    'wallets/transactions', StudentWalletTransactionViewSet,
    basename="students.wallets.transactions"
)
router.register('', StudentViewSet, basename="students")

urlpatterns = router.urls
