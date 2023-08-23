from django.db import models
from authentication.models import CustomUser

class Gun(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    count = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    def purchased_count(self):
        return self.user.count()
    
class Purchase(models.Model):
    gun = models.ForeignKey(Gun, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.gun.name