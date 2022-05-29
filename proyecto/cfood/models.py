from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserApp(models.Model):
    #user_sys = models.ForeignObject(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    name = models.CharField(max_length=70)
class Recipes(models.Model):
    recipeName = models.CharField(max_length=100)
    duration = models.IntegerField()
    description = models.CharField(max_length=400)

class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=100)
