from rest_framework import serializers
from django.db import transaction

from .models import Penjualan, ProdukItem
from user.serializers import SimpleUserSerializer
from bisnis.serializers import BarangSerializer



class ProdukItemserializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()

    class Meta:
        model = ProdukItem
        fields = [
            'id', 'penjualan',
            'barang', 'qty', 'harga',
            'item'
        ]
        read_only_fields = [
            'harga'
        ]


    def get_item(self, obj):
        return BarangSerializer(obj.barang).data


    def validate(self, attrs):
        penjualan = attrs.get('penjualan')
        qty =  attrs.get('qty',0)

        if penjualan.is_close:
            raise serializers.ValidationError({
                'detail': 'Penjualan already closed.'
            })
        
        if qty < 0:
            raise serializers.ValidationError({
                'detail': 'Cannot handle nagative quantity.'
            })
        return super().validate(attrs)
    

    def update(self, instance, validated_data):
        instance.qty = validated_data.get('qty', 0)
        instance.save()
        return instance
    

    @transaction.atomic
    def create(self, validated_data):
        penjualan = validated_data.get('penjualan')
        barang = validated_data.get('barang')
        qty = validated_data.get('qty', 1)

        item_obj, created = ProdukItem.objects.get_or_create(
            penjualan = penjualan, barang = barang
        )

        if not created:
            item_obj.qty += qty

        item_obj.harga = barang.harga    
        item_obj.save()

        return item_obj
    



class PenjualanSerializer(serializers.ModelSerializer):
    create_by = SimpleUserSerializer(read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Penjualan
        fields = [
            'id', 'create_by',
            'total',
            'is_close'
        ]
        read_only_fields = [
            'create_by', 'is_close'
        ]


    def get_total(self, obj):
        return obj.total()

    