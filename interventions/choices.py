from django.db import models


class InterventionStatus(models.TextChoices):
    """
    États possibles d'une intervention.
    """

    PENDING = "PENDING", "En attente"
    ASSIGNED = "ASSIGNED", "Assignée"
    IN_PROGRESS = "IN_PROGRESS", "En cours"
    ON_HOLD = "ON_HOLD", "En pause"
    COMPLETED = "COMPLETED", "Terminée"
    CANCELLED = "CANCELLED", "Annulée"


class InterventionPriority(models.TextChoices):
    """
    Niveaux de priorité d'une intervention.
    """

    LOW = "LOW", "Faible"
    MEDIUM = "MEDIUM", "Moyenne"
    HIGH = "HIGH", "Élevée"
    CRITICAL = "CRITICAL", "Critique"


class MaintenanceType(models.TextChoices):
    """
    Types de maintenance.
    """

    PREVENTIVE = "PREVENTIVE", "Préventive"
    CORRECTIVE = "CORRECTIVE", "Corrective"
    INSPECTION = "INSPECTION", "Inspection"