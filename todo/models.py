from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, User


class Item(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
	title = models.CharField(max_length = 40)
	description = models.TextField()
	check = models.BooleanField(default = False)
	date_added = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.title



