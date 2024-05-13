from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.token
