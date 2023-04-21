from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='covers/')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title