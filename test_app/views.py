from django.views import View
from django.http import HttpResponse


from random import random


class RandomNumberView(View):
   def get(self, request):
       number = random()
       return HttpResponse(number)
