from django.contrib import admin
from .models import Pizza, Size


# Register your models here.
@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    pass


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass