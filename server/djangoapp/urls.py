# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    path('', views.home, name='home'),        
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'), 

    # API endpoints (login etc.)
    path('login/', views.login_user, name='login'),
    # # path for registration

    # path for login
    # path(route='login', view=views.login_user, name='login'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
