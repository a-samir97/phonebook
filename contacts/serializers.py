from rest_framework import serializers
from .models import Contact, ContactNumber


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['numbers'] = instance.numbers.all().values_list('number', flat=True)
    #     return data


class ContactNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactNumber
        fields = "__all__"