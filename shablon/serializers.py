from rest_framework import serializers
from .models import Xizmatlar


class XizmatlarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xizmatlar
        fields = [
            'xizmat_turi',
            'ism_familiya',
            'hujjat',
            'izoh',
            'phone',
            'file',
        ]
