from django.urls import path

from first.models import Users

from django.urls import path, include
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
      model = Users
      fields = ("id",
    "job_title_id",
    "age",
    "first_name",
    "last_name",
    "father_name")
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
