from rest_framework import routers,serializers,viewsets
from flyo.models import data

class dataSerializer(serializers.ModelSerializer):
    class Meta:
        model=data
        fields= '__all__'