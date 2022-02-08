from rest_framework import serializers
from .models import project

class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = ('__all__')