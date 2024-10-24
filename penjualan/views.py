from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import Sum, F
from django.utils import timezone

from .serializers import PenjualanSerializer, ProdukItemserializer
from .models import Penjualan, ProdukItem



class PenjualanView(mixins.CreateModelMixin, mixins.ListModelMixin,
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    
    serializer_class = PenjualanSerializer
    queryset = Penjualan.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(create_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)

    @action(methods=['get'], detail=False)
    def todaySale(self, request, **kwargs):
        today = timezone.now()

        sumary = self.get_queryset().filter(
            create_on__date=today.date(), is_close=True
        ).aggregate(
            total = Sum(F('items__harga') * F('items__qty'))
        )

        return Response(sumary)

    @action(methods=['get'], detail=True)
    def items(self, request, *args, **kwargs):
        objs = self.get_object().items.filter(qty__gt=0)
        serializer = ProdukItemserializer(objs, many=True)

        return Response(serializer.data)
    

    @action(methods=['post'], detail=True)
    def bayar(self, request, **kwargs):
        obj = self.get_object()
        if not obj.is_close and obj.total() > 0:
            obj.is_close = True
            obj.save()
            return Response(self.get_serializer(obj).data)

        return Response({'detail': 'Invalid'} ,status=status.HTTP_400_BAD_REQUEST)
        

class ProdukItemView(mixins.CreateModelMixin, mixins.ListModelMixin,
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    
    serializer_class = ProdukItemserializer
    queryset = ProdukItem.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(qty__gt=0)
    
    
    