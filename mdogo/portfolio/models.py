from django.db import models

# Create your models here.
class Cartoon(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='cartoons/')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
