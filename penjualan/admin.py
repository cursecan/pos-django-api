from django.contrib import admin

from .models import Penjualan, ProdukItem


@admin.register(Penjualan)
class PenjualanAdmin(admin.ModelAdmin):
    list_display = [
        'create_on', 'is_close'
    ]
    list_filter = ['is_close']



@admin.register(ProdukItem)
class ProdukItemAdmin(admin.ModelAdmin):
    pass