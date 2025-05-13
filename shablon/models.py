from django.db import models

from shared.models import BaseModel


class XizmatTuri(models.TextChoices):
    NXX = "NXX", "NXX"
    MEDIA = "MEDIA", "MEDIA"
    SHARTNOMA = "SHARTNOMA", "SHARTNOMA"
    MAQOLA = "MAQOLA", "MAQOLA"


class Hujjat(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hujjat"
        verbose_name_plural = "Hujjat"
        ordering = ['name']


class Xizmatlar(BaseModel):
    xizmat_turi = models.CharField(max_length=20, choices=XizmatTuri.choices)
    ism_familiya = models.CharField(max_length=255)
    hujjat = models.ForeignKey(Hujjat, on_delete=models.CASCADE)
    izoh = models.TextField()
    phone = models.CharField(max_length=20)
    file = models.FileField(upload_to="xizmatlar/")

    class Meta:
        verbose_name = "Xizmatlar"
        verbose_name_plural = "Xizmatlar"
        ordering = ['xizmat_turi']


