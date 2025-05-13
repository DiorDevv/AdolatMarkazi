from django.contrib import admin

# Register your models here.
from .models import Hujjat, Xizmatlar


@admin.register(Hujjat)
class HujjatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Xizmatlar)
class XizmatlarAdmin(admin.ModelAdmin):
    list_display = ('id', 'xizmat_turi', 'ism_familiya', "phone")
    list_filter = ('ism_familiya', 'phone')
    search_fields = ['xizmat_turi', 'ism_familiya']
    list_per_page = 10
    list_editable = ['ism_familiya']
