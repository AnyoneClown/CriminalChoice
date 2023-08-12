from django.urls import path
from .views import RegisterView, home
 

urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('home/', home, name='')
]
