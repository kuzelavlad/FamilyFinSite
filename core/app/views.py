from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login

from app.models import User
from app.forms import SignUpForm


@api_view(['GET'])
def get_users(request):
    user = User.objects.all()
    for u in user:
        user_data = {
            "first_name": u.first_name,
            "last_name": u.last_name,
            "mail": u.email,
        }

    return Response(user_data)


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Замени 'home' на URL вашей главной страницы
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Пользователь успешно аутентифицирован
            return redirect('home')  # Замени 'home' на URL вашей главной страницы
        else:
            # Пользователь не найден или неправильный пароль
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')
