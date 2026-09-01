from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserConfirmation


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'phone_number',
        'is_staff',
    )
    list_filter = ('user_roles', 'auth_type', 'auth_status', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'phone_number', 'first_name', 'last_name')
    ordering = ('id',)

    fieldsets = BaseUserAdmin.fieldsets + (
        (
            'Custom Attributes',
            {
                'fields': (
                    'user_roles',
                    'auth_type',
                    'auth_status',
                    'phone_number',
                    'photo',
                )
            },
        ),
    )

    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (
            'Custom Attributes',
            {
                'fields': (
                    'user_roles',
                    'auth_type',
                    'auth_status',
                    'phone_number',
                    'email',
                )
            },
        ),
    )


@admin.register(UserConfirmation)
class UserConfirmationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'code',
        'verified_type',
        'is_confirmed',
        'expiration_type',
    )
    list_filter = ('verified_type', 'is_confirmed')
    search_fields = ('user__username', 'user__email', 'code')
    raw_id_fields = ('user',)