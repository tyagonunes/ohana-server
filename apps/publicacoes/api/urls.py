from rest_framework.routers import DefaultRouter
from apps.publicacoes.api.viewsets import *


router = DefaultRouter()
router.register(r'simbolos', SimboloViewSet, basename='simbolos')
router.register(r'procedimento-mediacao', ProcedimentoMediacaoViewSet, basename='procedimento_mediacao')
router.register(r'blog', BlogViewSet, basename='blog')

urlpatterns = router.urls