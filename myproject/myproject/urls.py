from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('employees', views.getEmployeeListOrCreate.as_view()),
	path('employees/<str:pk>', views.getEmployeeDetailsOrUpdateOrDelete.as_view()),
]