from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

PHONE_NUMBER_MAX_VALUE = 10000000000
PHONE_NUMBER_MIN_VALUE = 1000000000

def phone_number_validator(value):
    if (value > PHONE_NUMBER_MAX_VALUE 
        or value < PHONE_NUMBER_MIN_VALUE):
        
        return ValidationError(
            _("%(value)s is not a valid phone number"),
            params={"value": value},
        )
        



class ProfileViewChoices(models.TextChoices):
    LOCKED = "LKD", _("Locked")
    UNLOCKED = "UKD", _("UnLocked")
    
class ProfileStatusChoices(models.TextChoices):
    ACTIVE = "ACT", _("Active")
    DEACTIVE = "DCT", _("Deactive")
    
class ProfileDeleteChoices(models.TextChoices):
    YES = "Y", _("Yes")
    NO = "N", _("No")
    