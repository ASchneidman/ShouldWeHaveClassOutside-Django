from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {}
    return render(request, 'ClassOutside/index.html', context_dict)
