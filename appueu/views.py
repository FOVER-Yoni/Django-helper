import time
from django.shortcuts import render, HttpResponse
from appueu.models import cotegory, basedatel
import appueu.models
A = appueu.models
def index(request):
    context = {
        "keys": A.basedatel.objects.all()


                }
    return render(request, "tutorial/index.html", context)


def window(request):
    return render(request, "tutorial/window.html")



def hohoho(request):

    return render(request, "tutorial/hohoho.html")



