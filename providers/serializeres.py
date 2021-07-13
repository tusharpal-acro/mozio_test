from django.db.models import fields
from providers.models import Provider
from rest_framework import serializers


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"
        exclude = ()
