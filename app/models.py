from django.db import models
from django.utils import timezone

# Create your models here.
class Fort(models.Model):
    name = models.CharField(max_length=30,null=True)
    desc = models.TextField(max_length=3000,null=True)
    image = models.ImageField(upload_to='app/images',null=True)
    date_filled = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.pk)
    class Meta:
        verbose_name_plural = "Forts"
        verbose_name = "Fort"

class Team(models.Model):
    name = models.CharField(max_length=30,null=True)
    job = models.CharField(max_length=30,null=True)
    belogns_to = models.CharField(max_length=30,null=True)
    email = models.EmailField(null = True)
    def __str__(self):
        return str(self.pk)
    class Meta:
        verbose_name_plural = "Team"
        verbose_name = "Team"

    