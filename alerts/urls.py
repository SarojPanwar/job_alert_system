from django.urls import path
from alerts.views import alert_list

urlpatterns =[
    path("alerts/",alert_list ,name="alert_list"),
]