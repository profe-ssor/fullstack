from django.db import models

# Create your models here.
class Portfolio(models.Model):
    full_name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    avatar_url = models.URLField()
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.full_name
