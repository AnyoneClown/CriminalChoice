from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PurchaseForm
from django.contrib import messages
from .models import Gun, Purchase
from django.db.models import Count

@login_required(login_url="login")
def guns(request):
    form = PurchaseForm()
    return render(request, 'gun/armory.html', {'form': form})

def purchase_gun(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            gun = form.cleaned_data['gun']

            user = request.user
            if user.balance >= gun.price and gun.count > 0:
                user.balance -= gun.price
                user.save()

                purchase = Purchase(user=user, gun=gun)
                purchase.save()

                gun.count -= 1
                gun.save()

                messages.success(request, f"You have purchased {gun.name}.")
                return redirect('armory')
            else:
                messages.error(request, "Insufficient balance or out of stock for this purchase.")
    else:
        form = PurchaseForm(initial={'user': request.user})

    return render(request, 'gun/armory.html', {'form': form})


@login_required(login_url="login")
def weapons(request):
    user_purchases = Purchase.objects.filter(user=request.user).values('gun__name').annotate(total_quantity=Count('gun__name'))
    return render(request, 'gun/guns.html', {'user_purchases': user_purchases})