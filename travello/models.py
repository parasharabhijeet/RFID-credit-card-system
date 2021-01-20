from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
	
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	balance = models.PositiveIntegerField(default = 0)
	#rollno = models.CharField(null=True, blank=True, max_length=10)
	#request.user.id for getting user id
	def __str__(self):
		return str(self.user)

