from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
    
# views.py
# Условный пример при валидации формы, мы запускаем нашу задачу.
# ...
###from .tasks import supper_sum
#def form_valid(self, form):
   # ...
   # Запускаем нашу функцию при помощи метода delay - который, запустит task.
   # условно говоря celery обработает функцию в фоне.
 #   supper_sum.delay(5, 7)
 #   return super().form_valid(form)