from django.db import models




class Equipment(models.Model):
    reference = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    address = models.TextField()

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    qr_code = models.CharField(max_length=255, unique=True)
    backup_code = models.CharField(max_length=255, unique=True)

    installation_date = models.DateField()

    STATUS_CHOICES = [
    ("ACTIVE", "Active"),
    ("MAINTENANCE", "Maintenance"),
    ("OUT_OF_SERVICE", "Out of Service"),
    ]

    status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default="ACTIVE",
    )

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reference


class MaintenanceHistory(models.Model):

    equipment = models.ForeignKey(
        "equipments.Equipment",
        on_delete=models.CASCADE
    )

    intervention = models.ForeignKey(
        "interventions.Intervention",
        on_delete=models.CASCADE
    )

    maintenance_type = models.CharField(max_length=100)

    description = models.TextField()

    performed_at = models.DateTimeField()

    def __str__(self):
      return f"{self.equipment.reference} - {self.maintenance_type}"