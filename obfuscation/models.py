from django.db import models
# from django.forms import ModelForm, EmailInput, EmailField
# Create your models here.

class mailId(models.Model):
    email = models.EmailField(max_length=20)

    class Meta:
        db_table = "mails"


