from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated

from .serializers import NewPostSerializer

class CreateNewPostView(GenericAPIView, CreateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = NewPostSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)