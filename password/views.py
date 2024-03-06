from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Entry


def password_list(request):
    passwords = Entry.objects.all()
    return render(request, 'entry/password_list.html', {'passwords': passwords})


def password_add(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        try:
            name = request.POST['name']
            url = request.POST['url']
            username = request.POST['username']
            password = request.POST['password']
            Entry.objects.create(name=name, url=url,
                                 username=username, password=password)
            messages.success(request, f"New password added for {name}")
        except Exception as err:
            print('Error: ', err)
    return render(request, 'entry/password_add.html')
