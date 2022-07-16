from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Register

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']

        labels = {
            'first_name':'Full Name'
        }

    def __init__(self,*args,**kwargs):
        super(RegisterForm, self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class EditProfileForm(ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})













