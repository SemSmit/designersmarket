from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .forms import RoleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def requestview(request):
    """A view that submits the role form"""
    if request.method == 'POST':
        role_form = RoleForm(request.POST)
        if role_form.is_valid():
            role_form.save()
            
            messages.success(request, "You have successfully registered")
            return redirect(reverse('requestview'))
    else:
        """A view that displays the request page"""
        role_form = RoleForm()
        
        args = {'role_form': role_form,}
        return render(request, "request.html", args)
        
