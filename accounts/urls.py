from django.urls import path
from .views import login_user, logout_user, user_registration

app_name = 'accounts'
urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', user_registration, name="register"),
]
