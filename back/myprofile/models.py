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
        
# def email_validator(value)

# Create your models here.
class Profile(models.Model):
    username = models.CharField("User username", max_length=120, unique=True, primary_key=True)
    first_name = models.CharField("User firstname", max_length=120, blank=True, null=True)
    last_name = models.CharField("User lastname", max_length=120, blank=True, null=True)
    phone = models.IntegerField("User phone number", validators=[phone_number_validator])
    date_of_birth = models.DateField("User date of birth")
    email = models.EmailField("User email", max_length=255)
    password = models.TextField("User password")
    
    def __repr__(self) -> str:
        return "%s -> (%s %s)" % (self.username, self.first_name, self.last_name)
    
    def __str__(self) -> str:
        return repr(self)


class FBUser(models.Model):
    profile = models.OneToOneField(Profile, models.SET_NULL, related_name="fbuser")
    friends = models.ManyToManyField(Profile)
    

    def __repr__(self) -> str:
        return self.profile
    
    def __str__(self) -> str:
        return repr(self)

    