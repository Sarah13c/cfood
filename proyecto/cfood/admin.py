from django.contrib import admin

from .models import User
from .models import Recipes
from .models import Ingredients

admin.site.register(User)
admin.site.register(Recipes)
admin.site.register(Ingredients)
