from django.shortcuts import render
from .models import Hello

def home(request):
	hellos=Hello.objects.all()
	return render(request, 'yadav/home.html', {'hellos':hellos})
