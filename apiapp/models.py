
# api/models.py
from django.db import models

# Create your models here.

class XmlData(models.Model):
    data = models.TextField()  # Store raw XML data or parsed fields
    created_at = models.DateTimeField(auto_now_add=True)
