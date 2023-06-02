from django import forms


class CalculationForm(forms.Form):
    result = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control d-inline-block w-50'
        })
    )
