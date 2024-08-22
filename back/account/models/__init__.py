from uuid import uuid1
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


from account.models.setting import Setting
from account.models.profile import Profile
from account.models.unique import Unqiue
from account.models.token import APIToken




class Account(models.Model):
    
    # primary key,
    # generate unique for each user
    uid = models.OneToOneField(Unqiue, on_delete=models.SET_NULL, blank=True, null=True, related_name="account")
    
    # user information,
    # using default `authentication` model 
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="account")
    
    # profile = models.OneToOneField(, on_delete=models.SET_NULL, blank=True, null=True)
    
    # setting models
    setting = models.OneToOneField(Setting, on_delete=models.SET_NULL, blank=True, null=True,  related_name="account")
    
    
    # API Token
    token = models.OneToOneField(APIToken, on_delete=models.SET_NULL, blank=True, null=True, related_name="account")
    
    def save(self, *args, **kwargs) -> None:
        self.profile = Profile.objects.create()
        self.setting = Setting.objects.create()
        
        return super().save(*args, **kwargs)

    def __repr__(self) -> str:
        return "[%s]" % self.username
    
    def __str__(self) -> str:
        return "[%s]" % self.username


        """
    If user delete the account,
    then set `delete` to True.
    """
    deleted: bool = False