from django.shortcuts import redirect, render
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            password = form.cleaned_data['password1']
            user = authenticate(username=user.username, password=password)
            login(request, user)
            messages.success(request, 'Registro exitoso!')
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'snippets/sign_up.html', {'form': form})


def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')

        form = LoginForm()
        return render(request, 'snippets/sign_in.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Has iniciado sesion correctamente.')
                return redirect('/')
            else:
                messages.warning(request, 'Usuario o cotraseña incorrectos.')
        return render(request, 'snippets/sign_in.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('/')
