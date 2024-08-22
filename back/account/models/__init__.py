from typing import Any
from uuid import uuid1
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


from account.models.setting import Setting
from account.models.profile import Profile
from account.models.unique import Unique
from account.models.token import APIToken



class AccountManager(models.Manager):
    def create(self, **kwargs: Any) -> Any:
        return super().create(**kwargs)


class Account(models.Model):
    
    # primary key,
    # generate unique for each user
    uid = models.OneToOneField(Unique, on_delete=models.SET_NULL, blank=True, null=True, related_name="account")
    
    # user information,
    # using default `authentication` model 
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="account")
    
    # profile = models.OneToOneField(, on_delete=models.SET_NULL, blank=True, null=True)
    
    # setting models
    setting = models.OneToOneField(Setting, on_delete=models.SET_NULL, blank=True, null=True,  related_name="account")
    
    
    # API Token
    apitoken = models.OneToOneField(APIToken, on_delete=models.SET_NULL, blank=True, null=True, related_name="account")




    def __repr__(self) -> str:
        return "%s" % self.user.username
    
    def __str__(self) -> str:
        return "%s" % self.user.username


        """
    If user delete the account,
    then set `delete` to True.
    """
    deleted: bool = False