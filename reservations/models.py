from django.db import models
from django.contrib.auth.models import User
from book.models import Book

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} reserved {self.book.title} on {self.reserved_at}"