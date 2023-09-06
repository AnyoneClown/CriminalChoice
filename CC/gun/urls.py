from django.urls import path
from .views import guns, purchase_gun, weapons, organisation

urlpatterns = [
    path('armory/', guns, name='armory'),
    path('armory/purchase', purchase_gun, name='purchase_gun'),
    path('weapons/', weapons, name='weapons'),
    path('organisation/', organisation, name='organisation'),
]
