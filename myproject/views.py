# from django.http import HttpResponse
def about(request):
	return HttpResponse('This is page')

from django.shortcuts import render
def home(request):
	return render(request,'home.html',{'greeting': 'Hello'})