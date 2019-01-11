from django import  forms

class InputForm(forms.Form):
    name = forms.CharField(label='First Name',max_length=30)
    phone_number = forms.IntegerField(label='Phone Number')