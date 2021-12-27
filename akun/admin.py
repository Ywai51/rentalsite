from django.contrib import admin
from .models import NewAkun
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AkunAdminConfig(UserAdmin):
    model = NewAkun
    search_fields   = ('email','nama','no_hp')
    ordering        = ('-tanggal_akun',)
    list_display    = ('email','nama','no_hp','is_staff','last_login')
    list_filter     = ('is_staff','is_superuser')
    fieldsets = (
        (None, {
            "fields": (
                'email','nama','no_hp',
            ),
        }),
        ("Personal Info",{
            "fields": (
                'last_login','tanggal_akun',
            )
        }),
        ("Permission",{
            "fields": (
                'is_active','is_staff','is_superuser',
            )
        }),
        ("Password",{
            "fields": (
                'password',
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields': ('email','password1','password2','nama','no_hp','is_active','is_staff','is_superuser',)
        }),
    )

admin.site.register(NewAkun, AkunAdminConfig)
