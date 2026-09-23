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

@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def mark_notification_as_read(request,notification_id):

    notification = Notification.objects.filter(
        id=notification_id,
        user=request.user
    ).first()

    if notification is None:
        return Response(
               {"message":"Notification not found,"},        
                status=404
        )
    notification.is_read = True
    notification.save()

    return Response(
        {
            "message":"Notification marked as read"
        }
    )

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def unread_notification_list(request):

    notifications = Notification.objects.filter(
        user=request.user,
        is_read=False
    )
    if not notifications.exists():
        return Response(
            {
                "message":"There are no unread notifications for this user."
            }
        )
    serializer = NotificationSerializer(
        notifications,
        many=True
    )
    return Response(serializer.data)