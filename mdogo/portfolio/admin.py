from django.contrib import admin
from .models import Cartoon

# Register your models here.
@admin.register(Cartoon)

class CartoonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
