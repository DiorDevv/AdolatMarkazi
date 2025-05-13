# from django.contrib import admin
#
# # Register your models here.
# from django.apps import apps
#
# models = apps.get_models()
#
# for model in models:
#     try:
#         admin.site.register(model)
#     except:
#         pass
from django.contrib import admin

from singn.models import OTPCode, User


@admin.register(OTPCode)
class OTPCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'expiration_time')
    search_fields = ('code',)
    list_filter = ('expiration_time',)
    ordering = ('id',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_chat', 'created_at')
    search_fields = ('user_chat',)
    list_filter = ('created_at',)
    ordering = ('id',)