from django.forms import ModelForm
from myapp.models import *


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
