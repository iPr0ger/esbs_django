from rest_framework import serializers

from rms.models.dup.dup_studies import DupStudies


class DupStudiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DupStudies
        fields = '__all__'
