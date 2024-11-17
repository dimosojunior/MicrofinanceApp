from django.contrib import admin
from App.models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from import_export.admin import ImportExportModelAdmin

@admin.register(MyUser)
class MyUserAdmin(ImportExportModelAdmin):
    list_display=('username', 'email', 'phone', 'date_joined', 'last_login', 'is_admin', 'is_active')
    search_fields=('email', 'first_name', 'last_name')
    readonly_fields=('date_joined', 'last_login')
    filter_horizontal=()
    list_filter=('date_joined','last_login',)
    fieldsets=()

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email', 'username','phone', 'first_name', 'middle_name', 'last_name', 'company_name', 'phone', 'password1', 'password2'),
        }),
    )

    ordering=('email',)



@admin.register(OTP)
class OTPAdmin(ImportExportModelAdmin):
    list_display = ["id","user","otp", "created_at"]
    list_filter =["created_at"]
    search_fields = ["user"]


@admin.register(WatejaWote)
class WatejaWoteAdmin(ImportExportModelAdmin):
    list_display = ["id","JinaKamiliLaMteja","SimuYaMteja","EmailYaMteja","Mahali","KiasiAnachokopa","JumlaYaDeni","RejeshoKwaSiku", "Created"]
    list_filter =["Created"]
    search_fields = ["JinaKamiliLaMteja"]


class WatejaWoteCartAdmin(admin.ModelAdmin):
    list_display = ["id","JinaKamiliLaMteja","ordered", "total_price", "Created","Updated"]
    list_filter =["Created"]
    search_fields = ["JinaKamiliLaMteja"]

class WatejaWoteCartItemsAdmin(admin.ModelAdmin):
    list_display = ["id","JinaKamiliLaMteja","cart", "Mteja","KiasiChaRejeshoChaSiku", "Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["JinaKamiliLaMteja"]

admin.site.register(WatejaWoteCart, WatejaWoteCartAdmin)
admin.site.register(WatejaWoteCartItems, WatejaWoteCartItemsAdmin)

