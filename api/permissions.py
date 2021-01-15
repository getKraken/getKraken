from rest_framework import permissions
import logging

logger = logging.getLogger(__name__)

class IsSelfUser(permissions.BasePermission):
  def has_object_permissions(self, request, view, obj):
    return obj.username == request.user.username