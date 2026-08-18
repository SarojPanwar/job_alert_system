from django.urls import path
from jobs.views import job_list

urlpatterns = [
    path("jobs/",job_list, name ="job-list"),
]