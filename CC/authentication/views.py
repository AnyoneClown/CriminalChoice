from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.decorators import login_required
import random



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
    
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = CustomUser.objects.authenticate(request=request, email=email, password=password)

            if user is not None:
                user.is_active = True
                user.save()
                
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Invalid Email or Password')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
    
def logout_view(request):
    user = request.user
    user.is_active = False
    user.save()

    logout(request)
    return redirect('login')

def random_money(request):
    rand_money = random.randint(-1000, 1000)
    request.user.balance += rand_money
    request.user.save()
    messages.success(request, 'You gots $' + str(rand_money))

    return redirect('casino')
    

@login_required(login_url="login")
def home(request):
    return render(request, 'home.html')


@login_required(login_url="login")
def casino(request):
    return render(request, 'casino.html')