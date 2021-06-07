from django import forms
from .models import Measurements


class MeasurementModelForm(forms.ModelForm):
    destination = forms.CharField(label='Destination', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Measurements
        fields = ('destination',)
