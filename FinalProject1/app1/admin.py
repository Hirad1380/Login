from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display=('username','email','password_history_display')

    model=CustomUser
    fieldsets = UserAdmin.fieldsets+(
        (None, {
            'fields': (
                'security',
            ),
        }),
    )

    def password_history_display(self,obj):
        return ", ".join([entry.password for entry in obj.password_history.all()])
    
    password_history_display.short_description='Password History'
    
admin.site.register(CustomUser,CustomUserAdmin)