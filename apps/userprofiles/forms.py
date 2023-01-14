from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Profile, Link


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio',)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields['bio'].widget.attrs.update({
                "maxlength": "300",
                "placeholder": "Коротко о себе",
                'class': "textarea"
        })


class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ['url', 'title']

    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields['url'].widget.attrs.update({
                "placeholder": "Введите или вставьте Url",
                'class': "input"
            })
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields['title'].widget.attrs.update({
                "placeholder": "Назание для Url",
                'class': "input"
            })


