from django.shortcuts import render, redirect
from rest_framework.decorators import api_view

from app.forms import SignUpForm


@api_view(['GET'])
def home_page(request):
    registration_successful = request.session.pop('registration_successful', False)
    return render(request, 'home.html', {'registration_successful': registration_successful})


@api_view(['POST', 'GET'])
def registration(request):
    error_message = None

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['registration_successful'] = True
            return redirect('home_page')
        else:
            error_message = "Пожалуйста, исправьте следующие ошибки:"
    else:
        form = SignUpForm()

    return render(request, 'registration.html', {'form': form, 'error_message': error_message})
