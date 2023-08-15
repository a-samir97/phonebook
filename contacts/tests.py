from django.test import TestCase
from .models import Contact, ContactNumber


class ContactTest(TestCase):

    def setUp(self) -> None:
        self.contact = Contact.objects.create(name='test')
        self.contact_number = ContactNumber.objects.create(number="+2010911111111", contact=self.contact)

        self.contact_url = '/api/contacts/'

    def test_list_contact(self):
        response = self.client.get(self.contact_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.data), Contact.objects.count())

    def test_retrieve_contact_success_case(self):
        response = self.client.get(self.contact_url + f'{self.contact.id}/')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.data['numbers']), self.contact.numbers.count())

    def test_retrieve_contact_failure_case(self):
        response = self.client.get(self.contact_url + '1000/') # invalid id 

        self.assertEquals(response.status_code, 404)
