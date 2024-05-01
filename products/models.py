from django.db import models
from django.conf import settings
# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=120)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='images', blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='author')

    class Meta:
        db_table = 'product'
        ordering = ['-id']