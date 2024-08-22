from uuid import uuid1
from django.db import models
from django.utils.translation import gettext_lazy as _


class Unqiue(models.Model):
    id = models.CharField(_("id"), max_length=36, primary_key=True, unique=True)
    
    class Meta:
        app_label = "myprofile"