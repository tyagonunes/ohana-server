from rest_framework.routers import DefaultRouter
from apps.usuarios.api.viewsets import (
  UserViewSet
)

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = router.urls
