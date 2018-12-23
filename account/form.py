from django import forms
from user.form import RegisterForm
from .models import UserInfo


class SettingsForm(forms.ModelForm):
    
    class Meta:
        model = UserInfo
        fields = [
            'photo',
            'birthday', 
            'web', 
            'description', 
            'instagram', 
            'twitter', 
            'facebook', 
            'phone',
        ]
        widgets = {
            'web':forms.TextInput(attrs= {'placeholder':'Web'}),
            'description':forms.Textarea(attrs= {'placeholder':'Description'}),
            'instagram':forms.TextInput(attrs= {'placeholder':'Instagram'}),
            'twitter':forms.TextInput(attrs= {'placeholder':'Twitter'}),
            'facebook':forms.TextInput(attrs= {'placeholder':'Facebook'}),
            'phone':forms.TextInput(attrs= {'placeholder':'phone'}),
            'birthday':forms.SelectDateWidget()
        }
        labels = {
            'web':'',
            'description':'', 
            'instagram':'', 
            'twitter':'', 
            'facebook':'', 
            'phone':'',
            'photo':''
        }