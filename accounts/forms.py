from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password',
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password',
        'class': 'form-control',
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'Phone_Number', 'email', 'password', 'confirm_password']  # Include confirm_password

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name'
        self.fields['Phone_Number'].widget.attrs['placeholder'] = 'Enter your phone number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        # 'password' and 'confirm_password' placeholders are set in the field definition

        # Apply the 'form-control' class to all fields
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):  # Change method name from cleaned_data to clean
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # Check if passwords match
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match')

        return cleaned_data  # Return the cleaned data
