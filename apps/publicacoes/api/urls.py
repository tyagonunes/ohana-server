from rest_framework.routers import DefaultRouter
from apps.publicacoes.api.viewsets import *


router = DefaultRouter()
router.register(r'simbolo', SimboloViewSet, basename='simbolo')
router.register(r'classe-simbolo', ClasseSimboloViewSet, basename='classe_simbolo')
router.register(r'procedimento-mediacao', ProcedimentoMediacaoViewSet, basename='procedimento_mediacao')
router.register(r'blog', BlogViewSet, basename='blog')
router.register(r'categoria-blog', CategoriaBlogViewSet, basename='categoria_blog')
router.register(r'blog', BlogViewSet, basename='blog')
router.register(r'agenda-eventos', AgendaEventosViewSet, basename='agenda-eventos')
router.register(r'agenda-eventos-calendario', AgendaEventosCalendarioViewSet, basename='agenda-eventos-calendario')

urlpatterns = router.urls