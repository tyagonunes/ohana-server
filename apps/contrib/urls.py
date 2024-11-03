from django.urls import path, include


app_name = "contrib"
urlpatterns = [
    path("api/", include("apps.contrib.api.urls")),
]
