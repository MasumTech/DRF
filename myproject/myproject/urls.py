from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('employees', views.getEmployeeListOrCreate, 
		name="Employee List OR Create Employee"),
	path('employees/<str:pk>', views.getEmployeeDetailsOrUpdateOrDelete, 
		name="Employee Details OR Update OR Delete"),
]