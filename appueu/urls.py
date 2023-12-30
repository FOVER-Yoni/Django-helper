
from django.urls import path, include

app_name = 'appueu'

import appueu.views

view = appueu.views

urlpatterns = [
    path('', view.hohoho, name='hohoho')
]


