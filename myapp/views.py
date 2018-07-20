from django.shortcuts import render
from myapp.form import *
from myapp.models import *


def home(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
    userlist = User.objects.all()
    context = {
        'uf': form,
        'ul': userlist,
    }
    return render(request, 'home.html', context)
