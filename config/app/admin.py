from django.contrib import admin

from .models import Category, Cars

admin.site.register(Cars)
admin.site.register(Category)
