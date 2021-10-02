from rest_framework import serializers
from . models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Employee
		# fields=('firstName', 'lastName')
		fields = '__all__'	