from django.db import models
from django.utils import timezone
# Create your models here.


class Client(models.Model):
    fullname = models.CharField(max_length=100)
    birthdate = models.DateField()
    email = models.CharField(max_length=150, blank=True, null=True)
    phonenumber = models.CharField(max_length=20, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.fullname


class Visit(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='visits')
    visit_date = models.DateTimeField()
