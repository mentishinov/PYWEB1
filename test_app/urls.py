from django.urls import path

from .views import RandomNumberView

urlpatterns = [
   path('number/', RandomNumberView.as_view()),
]