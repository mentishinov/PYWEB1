from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


from datetime import datetime

class CurrentDateView(View):
   def get(self, request):
       html = f"{datetime.now()}"
       return HttpResponse(html)

class HelloView(View):
   def get(self, request):
       return HttpResponse("""<h1>Hello, World</h1>""")

class IndexView(View):
   def get(self, request):
       return render(request, 'common/index.html')