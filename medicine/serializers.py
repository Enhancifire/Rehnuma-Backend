from rest_framework import serializers
from .models import Medicine


class MedicineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medicine
        fields = [
            "name",
            "description",
            "cost_price",
            "selling_price",
            "quantity",
            "medicine_type",
        ]
