from django.shortcuts import render, redirect

# Create your views here.
def characters(request):
    return render(request, 'characters.html')