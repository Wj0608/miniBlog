from django.forms import ModelForm
from myapp.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
