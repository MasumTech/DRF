from . models import Employee
from . serializers import EmployeeSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class getEmployeeListOrCreate(mixins.ListModelMixin, mixins.CreateModelMixin, 
	generics.GenericAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	#authentication_classes = [SessionAuthentication, BasicAuthentication]
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)	 

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)	 

 
class getEmployeeDetailsOrUpdateOrDelete(mixins.RetrieveModelMixin, 
	mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)		
