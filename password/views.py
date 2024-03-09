from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Entry
from .forms import EntryForm


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


def password_delete(request, id):
    if request.method == 'GET':
        entry = Entry.objects.filter(id=id)
        entry.delete()
        return redirect('/')
    return redirect('password_list')


def password_update(request, id):
    entry = Entry.objects.get(id=id)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            redirect('password_list')
    else:
        form = EntryForm(instance=entry)
    return render(request, 'entry/password_update.html', {'form': form})
