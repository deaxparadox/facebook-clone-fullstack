from typing import Iterable, Self
from uuid import uuid1
from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models.extra import Time


class Unique(Time):
    id = models.CharField(_("id"), max_length=36, primary_key=True, unique=True)
    
    def __str__(self) -> str:
        return self.id
    


    def __eq__(self, value: Self) -> bool:
        return self.id == value.id
    
    def save(self, *args, **kwargs) -> None:
        self.id = str(uuid1())
        return super().save(*args, **kwargs)
