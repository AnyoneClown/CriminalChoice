from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm, BetForm
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

def play_game(request):
    if request.method == 'POST':
        form = BetForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']

            if amount > request.user.balance:
                messages.info(request, 'Not enough money')
                return redirect('play_game')
            
            # Calculate winning percentage and generate a random result
            win_percentage = random.randint(-90, 90) / 100
            rand_money = int(amount * win_percentage)
            
            request.user.balance += rand_money
            request.user.save()
            
            if rand_money > 0:
                messages.success(request, f"You won {str(rand_money)}$")
            else:
                messages.success(request, f"You lost {str(rand_money)}$")
            return redirect('casino')
    else:
        form = BetForm()
    return render(request, 'casino.html', {'form': form})

@login_required(login_url="login")
def home(request):
    return render(request, 'home.html')


@login_required(login_url="login")
def casino(request):
    return render(request, 'casino.html')