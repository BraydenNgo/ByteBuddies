from django import forms
# from django.forms import DateTimeInput, NumberInput, Textarea
from django.utils.safestring import mark_safe
from django.db import models
from .models import *

def logInForm(forms.Form):
    username = models.CharField("Username")
    password = models.CharField("Password")
