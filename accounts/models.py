from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    CATEGORY_CHOICES = (
    ("M", "Male"),
    ("F", "Female"),
    )
    first_name = None
    last_name = None
    email = models.EmailField(_("email address"),unique=True)
    name=models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    birth=models.DateField()
    sex= models.CharField(max_length=1, choices=CATEGORY_CHOICES, blank=True)
    intro=models.TextField(blank=True)
    
    REQUIRED_FIELDS = ["email","name","nickname","birth",]