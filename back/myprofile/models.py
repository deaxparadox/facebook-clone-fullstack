from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email

PHONE_NUMBER_MAX_VALUE = 10000000000
PHONE_NUMBER_MIN_VALUE = 1000000000

def phone_number_validator(value):
    if (value > PHONE_NUMBER_MAX_VALUE 
        or value < PHONE_NUMBER_MIN_VALUE):
        
        return ValidationError(
            _("%(value)s is not a valid phone number"),
            params={"value": value},
        )
        


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField("User firstname", max_length=120, blank=True, null=True)
    last_name = models.CharField("User lastname", max_length=120, blank=True, null=True)
    phone = models.IntegerField("User phone number", validators=[phone_number_validator], null=True, blank=True)
    date_of_birth = models.DateField("User date of birth", blank=True, null=True)
    
    def __repr__(self) -> str:
        return "Name -> [%s %s]" % (self.first_name, self.last_name)
    
    def __str__(self) -> str:
        return repr(self)
    
    
class ProfileViewChoices(models.TextChoices):
    LOCKED = "LKD", _("Locked")
    UNLOCKED = "UKD", _("UnLocked")
    
class ProfileStatusChoices(models.TextChoices):
    ACTIVE = "ACT", _("Active")
    DEACTIVE = "DCT", _("Deactive")
    
class ProfileDeleteChoices(models.TextChoices):
    YES = "Y", _("Yes")
    NO = "N", _("No")
    
    
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


class Account(models.Model):
    username = models.CharField("User username", max_length=120, unique=True, primary_key=True)
    password = models.TextField("User password", max_length=24)
    email = models.EmailField("User email", max_length=255)
    friends = models.ManyToManyField("self")
    
    
    profile = models.OneToOneField(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    setting = models.OneToOneField(Setting, on_delete=models.SET_NULL, blank=True, null=True)

    def __repr__(self) -> str:
        return "[%s]" % self.username
    
    def __str__(self) -> str:
        return repr(self)

    