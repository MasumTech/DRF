from django.db import models


class Employee(models.Model):
	firstName = models.CharField(max_length=10)
	lastName = models.CharField(max_length=10)
	employeeId = models.IntegerField()
	position = models.CharField(max_length=15)

	def __str__(self):
		return self.firstName