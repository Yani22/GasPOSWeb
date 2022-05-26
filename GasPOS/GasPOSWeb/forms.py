from django import forms
from .models import *

class EditEndUserForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("user_type", "profile_pic", "email", "first_name", "middle_name", "last_name", "birth_date", "gender_type", "age", "height_cm", "weight_kl", "address",)
