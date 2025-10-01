from django.contrib import admin

from .models import Category, Cars, Driver

admin.site.register(Cars)
admin.site.register(Category)
admin.site.register(Driver)
