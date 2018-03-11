from django.db import models

class book(models.Model):
	name = models.CharField(max_length = 500)
	author = models.CharField(max_length = 100)
	logo = models.FileField(max_length = 500, null=True)
	download = models.CharField(max_length = 500, null=True)

	def __str__(self):
		return self.name