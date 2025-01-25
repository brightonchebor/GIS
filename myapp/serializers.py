from rest_framework import serializers
from .models import Factory

# Serializer class which would parse json and create 
# Factory instances in database
class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = "__all__"

