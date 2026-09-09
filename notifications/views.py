from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from notifications.models import Notification
from notifications.serializers import NotificationSerializer

# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def notification_list(request):

    notifications =Notification.objects.filter(
        user = request.user
    )
    if not notifications.exists():
        return Response(
            {
                "message":"There are no notifications for this user."
            }
        )
    serializer = NotificationSerializer(
        notifications,
        many=True
    )
    return Response(serializer.data)

