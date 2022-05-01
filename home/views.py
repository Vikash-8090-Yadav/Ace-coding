from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
	return render(request,"home/index.html")

def term(request):
	return render(request,"home/term.html")

def article(request):
	return render(request,"home/article-details.html")

def privacy(request):
	return render(request,"home/privacy-policy.html")
