
from django.urls import path, include

app_name = 'users'

import users.views

view = users.views

urlpatterns = [
    path('login/', view.login, name='login'),
    path('register/', view.register, name='register'),
    path('profile/', view.profile, name='profile')
]


