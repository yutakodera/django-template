from rest_framework import serializers
from .models import CO2Data


class Co2DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CO2Data
        fields = "__all__"
