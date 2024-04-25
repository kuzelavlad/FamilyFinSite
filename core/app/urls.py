from django.urls import path
from app.views import get_users, login, home_page, registration
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('', home_page, name='home_page'),
    path('registration/', registration, name='registration'),
    path('login/', login, name='login'),
    path('api/users/', get_users, name='get_users'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
