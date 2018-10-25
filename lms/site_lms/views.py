from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'index.html')

def detalhe(request):
	return render(request, 'detalhe.html')

def lista_curso(request):
	return render(request, 'lista_curso.html')

def disciplina(request):
	return render(request, 'disciplina.html')

def noticias(request):
	return render(request, 'noticias.html')