from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,
        primary_key=True,)
	description=models.CharField(max_length=100,default='')
	city=models.CharField(max_length=100,default='')
	website=models.URLField(default='')
	phone=models.IntegerField(default=0)


