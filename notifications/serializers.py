from rest_framework import serializers
from notifications.models import Notification
from jobs.serializers import JobSerializer
class NotificationSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    company_name = serializers.CharField(
        source='job.company.name',
        read_only=True
    )
    job_detail_url = serializers.SerializerMethodField()
    class Meta:
        model = Notification
        fields =[
            "id",
            "job",
            "company_name",
            "job_detail_url",
            "message",
            "is_read",
            "created_at"

        ]
        read_only_fields =[
            "id",
            "created_at",
        ]

    def get_job_detail_url(self,obj):
        return f"/api/jobs/{obj.job.id}"