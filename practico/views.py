from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context

# Create your views here.
def prueba2(request):
	return render(request, "exam.html")