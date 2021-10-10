from rest_framework.routers import SimpleRouter

from .views import SchoolViewSet

router = SimpleRouter()
router.register('', SchoolViewSet, basename="schools")

urlpatterns = router.urls
