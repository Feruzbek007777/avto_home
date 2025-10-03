from django.contrib import admin

from .models import Category, Cars, Driver, Color

admin.site.register(Cars)
admin.site.register(Category)
admin.site.register(Driver)
admin.site.register(Color)
