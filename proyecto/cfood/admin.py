from django.contrib import admin

from .models import UserApp, Topic, Recipe
from .models import Ingredients

admin.site.register(UserApp)
admin.site.register(Recipe)
admin.site.register(Ingredients)
admin.site.register(Topic)
