from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE) #one user only have one profile
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.staff.username}-Profile'
# Create your models here.
