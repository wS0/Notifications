from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Notification
from .serializers import NotifySerializer


class SendView(APIView):
    def post(self, request):
        s = NotifySerializer(data=request.data)
        if not s.is_valid():
            return Response(s.errors, 400)
        n = Notification.objects.create(**s.validated_data)
        return Response({"id": n.id, "status": "queued"}, 202)
