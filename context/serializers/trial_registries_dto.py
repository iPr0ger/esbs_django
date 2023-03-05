from rest_framework import serializers

from context.models.trial_registries import TrialRegistries


class TrialRegistriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrialRegistries
        fields = '__all__'
