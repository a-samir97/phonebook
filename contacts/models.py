from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    name = models.CharField(max_length=256)


class ContactNumber(models.Model):
    number = PhoneNumberField()
    contact = models.ForeignKey(Contact, related_name='numbers', on_delete=models.CASCADE)
