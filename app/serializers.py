from django.core.mail import send_mail
from rest_framework import serializers


class EmailMessageClass:
    subject: str
    message: str
    recipients: str
    sender: str

    def __init__(self, subject: str, message: str, recipients: str, sender: str):
        self.subject = subject
        self.message = message
        self.recipients = recipients
        self.sender = sender


class MailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=100)
    message = serializers.CharField()
    recipients = serializers.CharField()
    sender = serializers.EmailField()

    def create(self, validated_data):
        email = EmailMessageClass(**validated_data)
        send_mail(
            email.subject,
            email.message,
            email.sender,
            email.recipients.split(',')
        )
        return email

    def update(self, instance, validated_data):
        instance.subject = validated_data.get('subject', instance.subject)
        instance.message = validated_data.get('message', instance.message)
        instance.recipients = validated_data.get('recipients', instance.recipients)
        instance.sender = validated_data.get('sender', instance.sender)

        send_mail(
            instance.subject,
            instance.message,
            instance.sender,
            instance.recipients.split(',')
        )

        return instance
