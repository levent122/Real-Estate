from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegisterForm(forms.Form):

    first_name = forms.CharField(max_length= 20, widget= forms.TextInput(attrs={'placeholder':'First Name'}),label='')
    last_name = forms.CharField(max_length= 20, widget= forms.TextInput(attrs={'placeholder':'Last Name'}),label='')
    email = forms.EmailField(widget= forms.EmailInput(attrs={'placeholder':'Email'}),label='')
    password = forms.CharField(max_length= 16, min_length= 8, widget= forms.PasswordInput(attrs={'placeholder':'Password'}),label='')
    confirm = forms.CharField(max_length= 16, min_length= 8, widget= forms.PasswordInput(attrs={'placeholder':'Confirm Password'}),label='')

    def clean(self):

        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')

        if User.objects.filter(username= email):

            self.add_error('email', "There is this email!")
        
        if password != confirm:

            self.add_error('confirm', "Password does not match")


class LoginFrom(forms.Form):

    email = forms.EmailField(widget= forms.EmailInput(attrs={'placeholder':'Email'}),label='')
    password = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder':'Password'}),label='')

    
    def clean(self):

        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = authenticate(username= email, password= password)

        if user:

            pass

        else:   

            raise forms.ValidationError("Email or password is wrong!")