from django.db import models

from shared.models import BaseModel


class Shaxrlar(models.TextChoices):
    IXTIYORIY = "IXTIYORIY", "IXTIYORIY"
    YANGI = "YANGI", "YANGI"


class Adabiyot(BaseModel):
    shaxrlar_turi = models.CharField(max_length=20, choices=Shaxrlar.choices)



