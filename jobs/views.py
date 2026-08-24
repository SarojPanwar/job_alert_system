from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from jobs.models import Job
from jobs.services import JobService
from jobs.serializers import JobSerializer
from rest_framework.pagination import PageNumberPagination

@api_view(["GET"])
def job_list(request):

    search = request.query_params.get("search")
    location = request.query_params.get("location")
    work_mode = request.query_params.get("work_mode")
    employment_type = request.query_params.get("employment_type")

    jobs = JobService.search_jobs(
        search=search,
        location=location,
        work_mode=work_mode,
        employment_type=employment_type,
    )
    paginator = PageNumberPagination()
    paginator.page_size  = 20

    page = paginator.paginate_queryset(
        jobs,
        request
    )
    serializer = JobSerializer(
        page,
        many=True
    )

    return paginator.get_paginated_response(serializer.data)

@api_view(["GET"])
def job_detail(request,job_id):

    job = get_object_or_404(
        Job,
        id=job_id,
        is_active=True
    )
    serializer = JobSerializer(job)

    return Response(serializer.data)
