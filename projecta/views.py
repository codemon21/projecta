from django.http import JsonResponse
from django.shortcuts import render

from projecta.models import User


# Create your views here.

def index(request):
    return render(request, 'index.html')


def newuser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if request.method == 'POST':
        createuser = User.objects.create(
            username=username,
            password=password
        )

        return JsonResponse({
            "saved": True
        })