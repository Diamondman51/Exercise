import re
from rest_framework.validators import ValidationError
from rest_framework import serializers

from .models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ("id", "first_name", "last_name", "email", "phone_number")

    def validate_phone_number(self, phone_number):
        phone_regex = r"^\+998\s?[0-9]{2}\s?[0-9]{3}[\s?-]?[0-9]{2}[\s?-]?[0-9]{2}$"
        phone_check = re.compile(phone_regex)
        if not phone_check.fullmatch(phone_number):
            raise ValidationError('Invalid phone number')
        return phone_number
    
    def validate_first_name(self, first_name):
        regex = re.compile(r"^[A-Za-zА-Яа-я]+$")
        print(regex.fullmatch(first_name))
        if regex.fullmatch(first_name):
            return first_name
        raise ValidationError('Last name is not valid. Only letters are allowed.')

    def validate_last_name(self, last_name):
        regex = re.compile(r"^[A-Za-zА-Яа-я]+$")
        print(regex.fullmatch(last_name))
        if regex.fullmatch(last_name):
            return last_name
        raise ValidationError('Last name is not valid. Only letters are allowed.')
