import binascii
import os

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class APIToken(models.Model):
    """
    The default authorization token model.
    """
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key


class TokenProxy(APIToken):
    """
    Proxy mapping pk to user pk for use in admin.
    """
    @property
    def pk(self):
        return self.user_id

    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")
