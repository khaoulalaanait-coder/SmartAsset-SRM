from django.db import models

class Report(models.Model):

    PRIORITY_CHOICES = [
        ("LOW", "Low"),
        ("MEDIUM", "Medium"),
        ("HIGH", "High"),
    ]

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("IN_PROGRESS", "In Progress"),
        ("REJECTED", "Rejected"),
        ("RESOLVED", "Resolved"),
    ]

    equipment = models.ForeignKey(
        "equipments.Equipment",
        on_delete=models.CASCADE,
        related_name="reports"
    )

    anomaly_type = models.CharField(max_length=100)
    description = models.TextField()

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="LOW"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    duplicate_counter = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Report #{self.id}"


class Photo(models.Model):

    report = models.ForeignKey(
        "reports.Report",
        on_delete=models.CASCADE,
        related_name="photos"
    )

    image = models.ImageField(upload_to="reports/")
    type = models.CharField(max_length=30)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo {self.id}"

   

class ReportHistory(models.Model):

    report = models.ForeignKey(
        "reports.Report",
        on_delete=models.CASCADE
    )

    old_status = models.CharField(max_length=30)

    new_status = models.CharField(max_length=30)

    changed_by = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE
    )

    changed_at = models.DateTimeField(auto_now_add=True)