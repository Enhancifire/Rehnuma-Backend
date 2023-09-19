from django.db import models
from django.utils.translation import gettext_lazy as _

from authentication.models import User


class UserProfile(models.Model):
    first_name = models.CharField(_("first name"), max_length=200, null=True)
    last_name = models.CharField(_("last name"), max_length=200, null=True)
    profilePicture = models.CharField(
        _("profile picture"),
        max_length=200,
        null=True
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "User Profiles"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.first_name
