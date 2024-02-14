from django.db import models


class DataCollected(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)
