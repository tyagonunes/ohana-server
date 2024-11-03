from rest_framework.viewsets import ModelViewSet
from apps.usuarios.models import User
from apps.usuarios.api.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()
    http_method_names = ['get', 'post', 'delete', 'put', 'patch', 'head']