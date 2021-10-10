from rest_framework.routers import SimpleRouter

from students.serializer import StudentParentSerializer

from .views import StudentViewSet

router = SimpleRouter()
router.register('', StudentViewSet, basename="students")
router.register(
    'parents/', StudentParentSerializer,
    basename="students.parents"
)

urlpatterns = router.urls
