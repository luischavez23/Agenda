from email.policy import default
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length = 150, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    priority = models.IntegerField(default=3)
    created_at = models.DateField(auto_now_add=True)
    estimated_end=models.DateField(blank=False, null=False)

    def __str__(self):
        return self.title