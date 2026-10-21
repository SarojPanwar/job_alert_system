from django.urls import path
from alerts.views import alert_list,alert_matching_jobs, delete_alert

urlpatterns =[
    path("alerts/",alert_list ,name="alert_list"),
    path("alerts/<int:alert_id>/jobs/",alert_matching_jobs, name="alert-matching-jobs"),
    path("alerts/<int:alert_id>/delete/",delete_alert, name="delete-alert"),
]