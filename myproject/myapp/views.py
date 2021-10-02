from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from . models import Employee
from . serializers import EmployeeSerializer

@api_view(['GET','POST'])
def getEmployeeListOrCreate(request):
	if request.method == "GET":
		getAllEmployees = Employee.objects.all()
		serializer = EmployeeSerializer(getAllEmployees, many=True)
		return Response(serializer.data)

	elif request.method == "POST":
		serializer = EmployeeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
def getEmployeeDetailsOrUpdateOrDelete(request, pk):
	try: 
		getTheEmployee = Employee.objects.get(id=pk)
	except Employee.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method =='GET':
		serializer = EmployeeSerializer(getTheEmployee, many=False)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = EmployeeSerializer(instance=getTheEmployee,
			data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)	
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

	elif request.method == 'DELETE':
		getTheEmployee.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)	

