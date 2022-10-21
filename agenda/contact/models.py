from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length = 100, blank=False, null=False)
    last_name = models.CharField(max_length = 150, blank=False, null=False)
    phone = models.CharField(max_length = 12, blank=True, null=True)
    mobile = models.CharField(max_length = 12, blank=False, null=False)
    email = models.EmailField()
    company = models.CharField(max_length = 100, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name