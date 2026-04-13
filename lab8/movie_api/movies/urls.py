from .views import MovieViewSet, DirectorViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'director', DirectorViewSet)
router.register(r'movies', MovieViewSet)

urlpatterns = router.urls