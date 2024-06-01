from django.forms import ModelForm, DateInput, DateTimeInput
from .models import Client, Visit


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'birthdate': DateInput(attrs={'type': 'date'}),
        }


class VisitForm(ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'
        widgets = {
            'visit_date': DateTimeInput(attrs={'type': 'date'}),
        }
