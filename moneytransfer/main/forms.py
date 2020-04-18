from django import forms
from register.models import UserProfile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'middle_initial', 'mailing_address',
        'country','email','phone_number','credit_card','bank_number',]
