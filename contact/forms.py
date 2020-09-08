from django import forms

CLASS_TYPE_CHOICES = [
    ('individualni', 'individualni'),
    ('grupni', 'grupni')
]
LEVEL_CHOICES = [
    ('ne govorim španski', 'ne govorim španski'),
    ('A1', 'A1'),
    ('A2', 'A2'),
    ('B1', 'B1'),
    ('B2', 'B2'),
    ('C1', 'C1')
]

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label='Ime i prezime ' )
    contact_email = forms.EmailField(required=True, label='Email ' )
    contact_number = forms.IntegerField(required=True, label='Broj telefona ' )
    message = forms.CharField(required=True, label='Poruka ', widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    class_type = forms.ChoiceField(choices=CLASS_TYPE_CHOICES, required=True, label='Tip časova ' )
    language_level = forms.ChoiceField(choices=LEVEL_CHOICES, required=True, label='Nivo španskog koji govorite ' )