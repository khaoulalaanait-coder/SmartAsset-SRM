from django.core.exceptions import ValidationError


MAX_NOTES_LENGTH = 1000


def validate_notes(value: str) -> None:
    """
    Vérifie que les notes ne dépassent pas la longueur maximale.
    """

    if value and len(value) > MAX_NOTES_LENGTH:
        raise ValidationError(
            f"Les notes ne peuvent pas dépasser {MAX_NOTES_LENGTH} caractères."
        )