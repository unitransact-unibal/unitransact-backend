from rest_framework.routers import SimpleRouter

from .views import StudentParentViewSet, StudentViewSet

router = SimpleRouter()
router.register('', StudentViewSet, basename="students")
router.register(
    'parents', StudentParentViewSet,
    basename="students.parents"
)

urlpatterns = router.urls
