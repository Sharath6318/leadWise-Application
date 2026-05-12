from rest_framework import serializers

from leadapplication.models import Lead


class LeadSerializer(serializers.ModelSerializer):

    class Meta:

        model = Lead

        fields = "__all__"

        read_only_fields=["id","last_contacted_date","created_at","updated_at"]

