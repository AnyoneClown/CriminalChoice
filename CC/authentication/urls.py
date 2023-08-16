from django.urls import path
from .views import RegisterView, login_view, logout_view, home, random_money, casino
 

urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('home/', home, name='home'),
    path('casino/', casino, name='casino'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('random_money/', random_money, name='random_money'),

]
