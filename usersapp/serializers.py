from rest_framework.serializers import HyperlinkedModelSerializer
from .models import MyUser

class MyUserModelSerioalizer(HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = [email_name, first_name, last_name]