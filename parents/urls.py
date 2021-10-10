from rest_framework.routers import SimpleRouter

from .views import ParentViewSet

router = SimpleRouter()
router.register('', ParentViewSet, basename="parents")

urlpatterns = router.urls
