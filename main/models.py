from django.db import models
from django.utils import timezone
# Create your models here.

class Personals(models.Model):
    first_name = models.CharField(max_length=1000, blank=True, null=True)
    last_name = models.CharField(max_length=1000, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    DOB = models.DateField(blank=True, null=True)

class Skills(models.Model):
    person = models.ForeignKey(Personals, on_delete=models.SET_NULL, blank=True, null=True)
    skill_name = models.CharField(max_length=1000, blank=True, null=True)
    skill_icon = models.ImageField(upload_to = "skills_img", blank=True, null=True)

class Visitors(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    visit_time = models.DateField(default=timezone.now)

class JobCategory(models.IntegerChoices):
    graphics = 1, 'graphics'
    webDev = 2, 'web Development'
    inDev = 3, 'in Development'

class Jobs(models.Model):
    category = models.IntegerField(default=JobCategory.inDev, choices=JobCategory.choices, blank=True, null=True)
    name = models.CharField(max_length=2000, null=True, blank=False)
    image = models.ImageField(upload_to = "jobs_img", blank=True, null=True)
    description = models.TextField(max_length=2000)

