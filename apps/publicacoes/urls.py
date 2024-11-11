from django.urls import path, include

app_name = "publicacoes"
urlpatterns = [
    path("api/", include("apps.publicacoes.api.urls")),
]