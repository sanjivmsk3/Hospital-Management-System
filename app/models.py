from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField()

    def __str__(self):
        return self.name

class User(AbstractUser):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    mobile = models.IntegerField(null=True, blank=True)



class Paitent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mobile = models.IntegerField()
    age = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def dat(self):
        date = self.date.date()
        if date == date:
            s = 0
            total = s + 1

        return total