from django.forms import ModelForm
from .models import Message

class DmForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message']


    def __init__(self,*args,**kwargs):
        super(DmForm, self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})