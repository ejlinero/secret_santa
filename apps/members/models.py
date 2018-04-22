from django.db import models


class Member(models.Model):
	name = models.CharField(max_length=16)
	email = models.EmailField()

	def __str__(self):
		return self.name