from django.urls import path, include
from apps.usuarios.views import GoogleLoginApi

app_name = "usuarios"
urlpatterns = [
    path("api/", include("apps.usuarios.api.urls")),
    path("login-google/", GoogleLoginApi.as_view(), name="login_google"),
]
