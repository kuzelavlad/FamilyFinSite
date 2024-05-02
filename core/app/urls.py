from django.urls import path
from app.views import home_page, registration
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('', home_page, name='home_page'),
    path('registration/', registration, name='registration'),
    # path('login/', login, name='login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
