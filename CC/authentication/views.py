from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.shortcuts import render



class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        
        return super(RegisterView, self).form_valid(form)
    
def home(request):
    return render(request, 'home.html')