from django.shortcuts import render
from .forms import RoleForm

# Create your views here.
def requestview(request):
    """A view that submits the role form"""
    if request.method == 'POST':
        role_form = RoleForm(request.POST)
        if role_form.is_valid():
            role_form.save()
    
    else:
        """A view that displays the request page"""
        role_form = RoleForm()
        
        args = {'role_form': role_form,}
        return render(request, "request.html", args)