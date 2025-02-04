from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('password', 'email', 'first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('password1', 'password2', 'email', 'first_name', 'last_name',),
                }),
    )
    ordering = ('email',)
    filter_horizontal = ()
