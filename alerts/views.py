from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from alerts.models import JobAlert
from alerts.serializers import JobAlertSerializer

# Create your views here.
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def alert_list(request):

    if request.method == "GET":

        alerts = JobAlert.objects.filter(
            user=request.user
        )

        serializer = JobAlertSerializer(
            alerts,
            many=True
        )

        return Response(serializer.data)

    elif request.method == "POST":

        serializer = JobAlertSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save(
                user=request.user
            )

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
