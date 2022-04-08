from django import forms

from .models import File
#from .models import User

class FileForm(forms.ModelForm):
    class Meta: 
        model = File
        fields = ('file_name', 'created_by', 'pdf', 'season', 'category', 'comments', 'preview',)
'''

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('user_name', 'email', 'password')
        widgets = {
            'password' : forms.PasswordInput(),
        }

'''
