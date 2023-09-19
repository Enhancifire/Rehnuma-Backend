from django.db import models
from django.utils.translation import gettext_lazy as _


class MedicineType(models.TextChoices):
    TABLET = "Tablet", _("Tablet")
    SYRUP = "Syrup", _("Syrup")
    INJECTION = "Injection", _("Injection")
    OINTMENT = "Ointment", _("Ointment")
    CAPSULE = "Capsule", _("Capsule")
    DROPS = "Drops", _("Drops")


class Medicine(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    quantity = models.IntegerField()
    medicine_type = models.CharField(max_length=100, choices=MedicineType.choices)

    class Meta:
        verbose_name_plural = "Medicines"

    def __str__(self):
        return self.name
