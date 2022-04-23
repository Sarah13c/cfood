from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=19)
    email = models.EmailField()

class Recipes(models.Model):
    recipeName = models.CharField(max_length=100)
    duration = models.IntegerField()
    description = models.CharField(max_length=400)

class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    ingredients = models.CharField(max_length=100)
