from django import forms
from django.forms import ModelForm

from db.models import Chore


class DateInput(forms.DateInput):
    input_type = 'date'


class ChoreForm(ModelForm):
    class Meta:
        model = Chore
        fields = ['name', 'cadence', 'next_due_date']
        widgets = {
            'next_due_date': DateInput(),
        }
