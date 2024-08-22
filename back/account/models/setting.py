from django.db import models
from django.contrib.auth.models import User

from account.helpers import (
    ProfileDeleteChoices,
    ProfileStatusChoices,
    ProfileViewChoices
)



    
class Setting(models.Model):
    
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
    delete = models.CharField(
        max_length=1,
        choices=ProfileDeleteChoices,
        default=ProfileDeleteChoices.NO
    )


    def is_deleted(self) -> bool:
        return self.delete == "YES"
    
