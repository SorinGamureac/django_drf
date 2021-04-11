from rest_framework.viewsets import ModelViewSet
from .models import MyUser
from .serializers import MyUserModelSerioalizer

class MyUserModelViewSets(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserModelSerioalizer

