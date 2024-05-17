from rest_framework import serializers
from .models import imgAPI


class imgSerializer(serializers.ModelSerializer):
    class Meta:
        model = imgAPI
        fields = (
            'id',
        )