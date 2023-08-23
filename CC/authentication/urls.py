from django.urls import path
from .views import RegisterView, login_view, logout_view, home, casino, play_game
 

urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('home/', home, name='home'),
    path('casino/', casino, name='casino'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('casino/play_game', play_game, name='play_game'),

]
