from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'motivos-reprovacao', MensagensReprovacaoDocumentosViewSet, basename='motivos-reprovacao')

urlpatterns = router.urls