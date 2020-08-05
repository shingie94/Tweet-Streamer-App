from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_me': "Hello i am from views.py"}
    return render(request,'app/index.html', context=my_dict)
