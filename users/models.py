from django.db import models
from uuid import uuid4


class User(models.Model):
    # uid = models.UUIDField(primary_key=True, default=uuid4)
    id = models.BigAutoField(auto_created=True, primary_key=True)
    username = models.CharField(max_length=40)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64, unique=True)
