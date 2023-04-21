from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

class BookDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_update(self, serializer):
        if self.request.user.is_staff:
            serializer.save()
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def perform_destroy(self, instance):
        if self.request.user.is_staff:
            instance.delete()
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
