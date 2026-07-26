from django.utils import timezone


def get_current_datetime():
    """
    Retourne la date et l'heure actuelle.
    """
    return timezone.now()


def calculate_duration(start, end):
    """
    Calcule la durée d'une intervention.
    """
    if start and end:
        return end - start
    return None