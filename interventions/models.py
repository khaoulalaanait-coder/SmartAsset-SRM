from django.db import models


class Intervention(models.Model):

    STATUS_CHOICES = [
        ("ASSIGNED", "Assigned"),
        ("IN_PROGRESS", "In Progress"),
        ("DONE", "Done"),
    ]

    report = models.ForeignKey(
        "reports.Report",
        on_delete=models.CASCADE,
        related_name="interventions"
    )

    technician = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="assigned_interventions"
    )

    coordinator = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="coordinated_interventions"
    )

    assigned_at = models.DateTimeField()
    started_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    notes = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ASSIGNED"
    )

    def __str__(self):
        return f"Intervention {self.id}"

  
class Notification(models.Model):

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    title = models.CharField(max_length=200)

    message = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title