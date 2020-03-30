from django.shortcuts import render


# Create your views here.

def home(request):
    """
    A view for home page
    """
    return render(request, "index.html")