from rest_framework import generics
from .models import Xizmatlar
from .serializers import XizmatlarCreateSerializer


class XizmatlarCreateView(generics.CreateAPIView):
    queryset = Xizmatlar.objects.all()
    serializer_class = XizmatlarCreateSerializer
