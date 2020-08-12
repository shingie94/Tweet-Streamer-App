from django.http import HttpResponse
from django.shortcuts import render
from django.views import View, ListView

# Create your views here.
class MyView(View):
    def get(self, request):
        # <view logic>
        my_dict = {'insert_me': "Hello i am from views.py"}
        return render(request,'app/index.html', context=my_dict)
