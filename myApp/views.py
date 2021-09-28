from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_word(request):
    # return HttpResponse('Olá Mundo!')
    return render(request, 'curriculo.html')