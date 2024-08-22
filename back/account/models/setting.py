from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from account.helpers import (
    ProfileDeactivateChoices,
    ProfileStatusChoices,
    ProfileViewChoices
)

from account.models.extra import Time


    
class Setting(Time):
    
    locked = models.CharField(
        max_length=3,
        choices=ProfileViewChoices,
        default=ProfileViewChoices.UNLOCKED
    )
    status = models.CharField(
        max_length=3, 
        choices=ProfileStatusChoices, 
        default=ProfileStatusChoices.ACTIVE
    )
    deactivate = models.CharField(
        max_length=1,
        choices=ProfileDeactivateChoices,
        default=ProfileDeactivateChoices.NO
    )
    
    deleted = models.BooleanField(_("deleted"), default=False)


    def is_deleted(self) -> bool:
        return self.delete == "YES"
    
