from rest_framework import mixins, viewsets


from .serializers import BarangSerializer
from .models import Barang



class BarangView(mixins.ListModelMixin, mixins.CreateModelMixin,
                 mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    
    serializer_class = BarangSerializer
    queryset = Barang.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()

        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(nama_barang__contains=q)

        return queryset



