from django.core.mail import send_mail
from rest_framework import permissions

from rest_framework.response import Response
from rest_framework.views import APIView

from app.serializers import MailSerializer


class EmailSender(APIView):
    permission_classes = [permissions.AllowAny]
    def get_serializer(self, *args, **kwargs):
        return MailSerializer(*args, **kwargs)

    def post(self, request, format=None):
        serializer = MailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success'}, status=200)
        return Response(serializer.errors,  status=400)
