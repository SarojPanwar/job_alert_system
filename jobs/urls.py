from django.urls import path
from jobs.views import job_list,job_detail

urlpatterns = [
    path("jobs/",job_list, name ="job-list"),
    path("jobs/<int:job_id>",job_detail,name="job_detail"),
]