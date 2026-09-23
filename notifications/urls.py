from django.urls import path
from notifications.views import notification_list,mark_notification_as_read, unread_notification_list
urlpatterns=[
    path("notifications/",notification_list, name="notification-list"),
    path("notifications/<int:notification_id>/read/",mark_notification_as_read, name="mark-notification-as-read"),
    path("notifications/unread/",unread_notification_list, name="unread-notification-list"),
]