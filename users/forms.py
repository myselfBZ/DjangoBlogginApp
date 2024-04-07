from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', "password"] 


class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['bio'].widget.attrs['class'] = 'form-control form-control-lg'
    class Meta:
        model = Profile
        fields = ['image', 'bio']