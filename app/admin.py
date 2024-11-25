from django.contrib import admin
from .models import feedback
from app.models import profile_data
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(feedback)

class profile_data_Inline(admin.StackedInline):
    model = profile_data
    can_delete = False
    verbose_name_plural = 'profile_datas'

class CustomaizedUserAdmin (UserAdmin):
    inlines = (profile_data_Inline,)

admin.site.unregister(User)
admin.site.register(User, CustomaizedUserAdmin)

admin.site.register(profile_data)