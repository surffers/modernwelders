from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ("email",)
        widgets = {
            "email": forms.TextInput(attrs={"class": "input", "placeholder": "E-mail adress"})
        }
        labels = {
            "email": ''
        }