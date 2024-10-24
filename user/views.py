from rest_framework import mixins, viewsets
from rest_framework.response import Response

from .models import User
from .serializers import SimpleUserSerializer



class ProfileView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = SimpleUserSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.id)
        serializer = self.get_serializer(user, many=False)
        return Response(serializer.data)