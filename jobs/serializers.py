from rest_framework import serializers

from jobs.models import Job


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = [
            "id",
            "company",
            "title",
            "location",
            "experience",
            "employment_type",
            "work_mode",
            "apply_url",
            "department",
            "office",
            "posted_date",
            "description",
            "skills",
            "is_active",
            "created_at",
            "updated_at",
        ]