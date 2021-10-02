from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from myapp.views import EmployeeList,EmployeeDetail 


urlpatterns = [
    path('admin/', admin.site.urls),
	path('employees', EmployeeList.as_view()), 
	path('employees/<str:pk>', EmployeeDetail.as_view()), 
]
