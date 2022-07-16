from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['owner']

        labels ={
            'time_reminder': 'Time Reminder(DD/MM/YY/ HH/MM/SS)'
        }

    def __init__(self,*args,**kwargs):
        super(TodoForm, self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})