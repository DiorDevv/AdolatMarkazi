from django.urls import path
from .views import XizmatlarCreateView

urlpatterns = [
    path('xizmatlar/create/', XizmatlarCreateView.as_view(), name='xizmatlar-create'),
]
