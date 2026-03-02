from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def feedback(request):
    return render(request, 'feedback.html')