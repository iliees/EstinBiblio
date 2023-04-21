from django.db import models
from django.contrib.auth.models import AbstractUser
from book.models import Book

class CustomUser(AbstractUser):
    # Ajout de champs supplémentaires pour le modèle User
    photo = models.ImageField(upload_to='users/', blank=True, null=True)
    books_borrowed = models.ManyToManyField(Book, blank=True, related_name='borrowers')
    borrowed_history = models.ManyToManyField(Book, blank=True, related_name='borrowed_users')
    comments = models.ManyToManyField(Book, blank=True, through='Comment')

class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    stars = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
