from rest_framework import serializers

from .models import Barang

# {
#             "id": 1,
#             "create_on": "2024-10-22T04:57:33.405363Z",
#             "update_on": "2024-10-22T04:57:33.405411Z",
#             "nama_barang": "Testing barang 1",
#             "deskripsi": "",
#             "barcode": "",
#             "stok": 0,
#             "harga": 5000
#         }

class BarangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barang
        fields = [
            'id', 'nama_barang',
            'deskripsi', 'barcode',
            'stok', 'harga'
        ]
        read_only_fields = [
            'stok', 'barcode'
        ]