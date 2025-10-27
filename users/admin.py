from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'is_staff', 'is_superuser', 'is_active',]

    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal Information', {'fields': ('first_name', 'last_name', 'birth_date',)}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions',)}),
        ('Important Dates', {'fields': ('last_login', 'date_joined',)}),
    )

    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'first_name', 'last_name', 'birth_date', 'password1', 'password2',)}),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)


