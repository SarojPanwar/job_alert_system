from rest_framework import serializers

from alerts.models import JobAlert


class JobAlertSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobAlert
        fields = [
            "id",
            "keywords",
            "location",
            "work_mode",
            "employment_type",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]