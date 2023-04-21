from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, Comment
from .serializers import UserSerializer, CommentSerializer
from rest_framework import generics
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        # Afficher les commentaires de l'utilisateur
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        else:
            return queryset.filter(id=self.request.user.id)
#pour afficher le profile d'un utilisateur        
class UserProfileView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        # Afficher les commentaires de l'utilisateur
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        else:
            return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Ajouter l'utilisateur qui crée le commentaire
        serializer.save(user=self.request.user)
