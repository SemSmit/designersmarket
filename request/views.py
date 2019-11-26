from django.shortcuts import render

# Create your views here.
def requestview(request):
    """A view that displays the home page"""
    return render(request, "request.html")