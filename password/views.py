from django.shortcuts import render
from .models import Entry


def password_list(request):
    passwords = Entry.objects.all()
    return render(request, 'entry/password_list.html', {'passwords': passwords})
