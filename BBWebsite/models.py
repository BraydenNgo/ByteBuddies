from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    # Binds to User Account
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Inputed from Account page
    profilePic = models.ImageField(upload_to='photos/')
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    age = models.IntegerField()
    college = models.CharField(max_length=60)
    major = models.CharField(max_length=40)
    pronoun = models.CharField(max_length=20)
    
class Personality(models.Model):
     # Binds to User Account
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Inputed from Personality page
    extraversionChoices = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    extraversion = models.IntegerField(choices=extraversionChoices)
    smokeOrDrinkChoices = (
        ('no', 'No'),
        ('smoke', 'Smoke'),
        ('drink', 'Drink'),
        ('both', 'Both'),
    )
    smokeOrDrink = models.CharField(max_length=20, choices=smokeOrDrinkChoices)
    cleanlinessChoices = (
        ('neat', 'Neat'),
        ('neutral', 'Neutral'),
        ('messy', 'Messy'),
    )
    cleanliness = models.CharField(max_length=20, choices=cleanlinessChoices)
    socialChoices = (
        ('friendly', 'Friendly and outgoing'),
        ('moderate', 'Moderately Social'),
        ('quiet', 'Quiet and Reserved'),
    )
    social = models.CharField(max_length=20, choices=socialChoices)
    genderPreference = (
        ('single', 'Single Gender'),
        ('mixed', 'Mixed Gender'),
    )
    genderPreference = models.CharField(max_length=20, choices=socialChoices)
    

class Internship(models.Model):
     # Binds to User Account
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Inputed from Internship page
    company = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    season = models.CharField(max_length=40)
    budget = models.CharField(max_length=40)
    