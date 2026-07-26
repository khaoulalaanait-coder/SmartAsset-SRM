from rest_framework.permissions import BasePermission


class IsCoordinator(BasePermission):
    """
    Autorise uniquement les coordinateurs.
    """

    message = "Seuls les coordinateurs sont autorisés."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and getattr(request.user, "role", None) == "COORDINATOR"
        )


class IsTechnician(BasePermission):
    """
    Autorise uniquement les techniciens.
    """

    message = "Seuls les techniciens sont autorisés."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and getattr(request.user, "role", None) == "TECHNICIAN"
        )