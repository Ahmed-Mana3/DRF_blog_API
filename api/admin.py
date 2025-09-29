from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Blog

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ["username", "email", "first_name", "last_name"]


class BLogAdmin(admin.ModelAdmin):
    list_display = ["title", "is_draft", "category", "publish_date"]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Blog, BLogAdmin)


