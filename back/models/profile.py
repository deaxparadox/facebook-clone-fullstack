from django.db import models


from models.helpers import phone_number_validator

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
    
    
    class Meta:
        app_label = "myprofile"