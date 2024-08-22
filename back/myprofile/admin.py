from django.contrib import admin

from models.profile import Profile
from models.setting import Setting
from myprofile.models import Account


class ProfileAdmin(admin.ModelAdmin):
    pass

class SettingAdmin(admin.ModelAdmin):
    pass 

class AccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(Account, AccountAdmin)