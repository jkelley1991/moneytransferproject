from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    middle_initial = models.CharField(max_length = 1)
    mailing_address = models.CharField(max_length = 100)
    country = models.CharField(max_length = 30)
    email = models.EmailField()
    phone_number = models.IntegerField(max_length = 10, null = True)
    credit_card = models.IntegerField(max_length = 16,null = True)
    bank_number = models.IntegerField(max_length = 16,null = True)
