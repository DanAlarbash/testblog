from django.db import models

class DDD(models.Model):
    name = models.CharField(max_length=50)
    CV = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
