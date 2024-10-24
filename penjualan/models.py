from django.db import models
from django.db.models import Sum, F

from base.models import CommondBase
from bisnis.models import Barang
from user.models import User

    
class Penjualan(CommondBase):
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_close = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)
    

    def total(self):
        summary = self.items.aggregate(
            total = Sum(F('harga') * F('qty'))
        )
        return summary['total']


class ProdukItem(CommondBase):
    penjualan = models.ForeignKey(Penjualan, on_delete=models.CASCADE, related_name='items')
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    harga = models.PositiveIntegerField(default=0)
    qty = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.barang.nama_barang



    