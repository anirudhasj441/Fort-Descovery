from django.db import models
from django.utils import timezone

# Create your models here.
class Fort(models.Model):
    name = models.CharField(max_length=30,null=True)
    desc = models.TextField(max_length=3000,null=True)
    image = models.ImageField(upload_to='app/images',null=True)
    sc1 = models.ImageField(upload_to='app/images',null=True)
    sc2 = models.ImageField(upload_to='app/images',null=True)
    sc3 = models.ImageField(upload_to='app/images',null=True)
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

    
class ContactForm(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.EmailField()
    contact = models.CharField(max_length=30,null=True)
    message = models.TextField(max_length=3000,null=True)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.pk)
    class Meta:
        verbose_name_plural = "Messages"
        verbose_name = "Message"

class Profile(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    contact = models.CharField(max_length=30,null=True,blank=True)
    about = models.TextField(max_length=3000,null=True,blank=True)
    pic = models.ImageField(upload_to = 'app/images/profil',null=True,blank=True)
    github = models.CharField(max_length=100,null=True,blank=True)
    linkedin = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.pk)
    class Meta:
        verbose_name_plural = "Profile"
