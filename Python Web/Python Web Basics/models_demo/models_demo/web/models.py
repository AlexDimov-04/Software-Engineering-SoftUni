from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=41)
    descriptions = models.TextField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"ID -> {self.pk} -> Names -> {self.full_name}"