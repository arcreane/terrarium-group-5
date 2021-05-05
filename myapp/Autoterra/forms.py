from django import forms

class Humidite(forms.Form):
    Humidite_min = forms.IntegerField(label='Humidite minimale',min_value=0)
    Humidite_max = forms.IntegerField(label='Humidite maximale',max_value=100)