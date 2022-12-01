from django.db import models


# Create your models here.
class User(models.Model):
    """Model representing a book genre."""
    username = models.CharField(max_length=30, help_text='enter your username')
    password = models.CharField(max_length=30, help_text='enter your password')

    def __str__(self):
        return self.username
