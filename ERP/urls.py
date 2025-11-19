
from django.urls import path
from . views import (
    EmployeerListCreateGenaric,
    EmployerRetriveUpdateDestroyeGeneric,
    EmployeeAPI,
    EmployeesDetailsAPi
    
)

urlpatterns = [
    # Employer (Generic Views)
    path('employers-Creation-and-listing/',EmployeerListCreateGenaric.as_view(),name="emplyer-list"),
    path('employers-details-delete/<int:pk>/',EmployerRetriveUpdateDestroyeGeneric.as_view(),name="emplyer-details"),
    
    
    path("employees/",EmployeeAPI.as_view(),name='employee-list'),
    path("employees/<int:pk>/",EmployeesDetailsAPi.as_view(),name="employee-details")
    
]
