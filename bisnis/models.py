from django.db import models

from base.models import CommondBase



class Barang(CommondBase):
    nama_barang = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=100, blank=True)
    barcode = models.CharField(max_length=36, blank=True)
    stok = models.PositiveSmallIntegerField(default=0)
    harga = models.PositiveIntegerField()

    def __str__(self):
        return self.nama_barang


