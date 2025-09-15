from django.shortcuts import render

# Create your views here.
def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

def kiwobar(request):
    return render(request, 'home/kiwobar.html')

def guinnessbar(request):
    return render(request, 'home/guinnessbar.html')

def mobilebar(request):
    return render(request, 'home/mobilebar.html')

def tabletopbar(request):
    return render(request, 'home/tabletopbar.html')