from django.contrib import admin

# Register your models here.
from account.models.profile import Profile
from account.models.setting import Setting
from account.models import Account


class ProfileAdmin(admin.ModelAdmin):
    pass

class SettingAdmin(admin.ModelAdmin):
    pass 

class AccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(Account, AccountAdmin)