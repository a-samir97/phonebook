from rest_framework.viewsets import ModelViewSet
from .models import Contact, ContactNumber
from .serializers import ContactSerializer, ContactNumberSerializer


class ContactModelViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        response.data['numbers'] = instance.numbers.all().values_list('number', flat=True)
        return response


class ContactNumberModelViewSet(ModelViewSet):
    queryset = ContactNumber.objects.all()
    serializer_class = ContactNumberSerializer
