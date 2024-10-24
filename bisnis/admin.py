from django.contrib import admin

from .models import Barang



@admin.register(Barang)
class BarangAdmin(admin.ModelAdmin):
    pass