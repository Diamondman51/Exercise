import re
from django import forms

from .models import Users


class AddUserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ("first_name", "last_name", "email", "phone_number")
    
    def clean(self):
        cleaned_data = super().clean()
        
    def clean_first_name(self):
        regex = re.compile(r"^[A-Za-zА-Яа-я]+$")
        first_name = self.cleaned_data.get("first_name", '')
        print(regex.fullmatch(first_name))
        if regex.fullmatch(first_name):
            return first_name
        raise forms.ValidationError('First name is not valid. Only letters are allowed.')

    def clean_last_name(self):
        regex = re.compile(r"^[A-Za-zА-Яа-я]+$")
        last_name = self.cleaned_data.get("last_name", '')
        print(regex.fullmatch(last_name))
        if regex.fullmatch(last_name):
            return last_name
        raise forms.ValidationError('Last name is not valid. Only letters are allowed.')

    def clean_phone_number(self):
        phone = self.cleaned_data.get("phone_number", '')
        phone_regex = r"^(\+998\s?)?[0-9]{2}\s?[0-9]{3}[\s?-]?[0-9]{2}[\s?-]?[0-9]{2}$"
        phone_check = re.compile(phone_regex)
        if not phone_check.fullmatch(phone):
            raise forms.ValidationError('Invalid phone number')
        return phone
    