from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .models import Employee,Employer
from .serializers import EmployeeSerializer,EmployerSerializer
# Create your views here.

# ---------------- EMPLOYER (Generic Views) ----------------
class EmployeerListCreateGenaric(generics.ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    
    def create(self, request, **kwargs):
        try:
            super().create(request, **kwargs)
            return Response({"status":"success","response_code":201,"message":"created successfully"})
        except Exception as e:
            return Response({"status":"success","response_code":status.HTTP_201_CREATED,"message":str(e)})
    
    def list(self,request,**kwargs):
        try:
            response = super().list(request,**kwargs)
            return Response({"status":"success","response_code":200,"data":response.data})
        except Exception as e:
            return Response({"status":"failed","response_code":400,"message":str(e)})
    
    
    
class EmployerRetriveUpdateDestroyeGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    
    def update(self,request,**kwargs):
        try:
            response = super().update(request,**kwargs)
            return Response({"status":"updation success",
                             "response_code":200,
                             "message":"updation completed successfully!",
                             "data": response.data})
        except Exception as e:
            return Response({"status":"updation failed",
                             "response_code":400,
                             "message":str(e)})
    
    
    def delete(self,request,**kwargs):
        try:
            response = super().delete(request,**kwargs)
            return Response({"status":"item deleted","message":"item deleted","response_code":200})
        except Exception as e:
            return Response({"status":"updation failed",
                             "response_code":400,
                             "message":str(e)})
    

# ---------------- EMPLOYEE (API Views) ----------------

class MyPagenation(PageNumberPagination):
    page_size = 5

class EmployeeAPI(APIView):

    
    def get(self,request):
        employees = Employee.objects.all().order_by('id')
        paginator = MyPagenation()
        pagenated_qs = paginator.paginate_queryset(employees,request)
        seralizers = EmployeeSerializer(pagenated_qs,many=True)
        return paginator.get_paginated_response(seralizers.data)
    
    
    def post(self,request):
        try:
            data = request.data
            if not data['name']:
                return Response({"status":"failed","response_code":status.HTTP_400_BAD_REQUEST,"message":"sorry, name is mandatory"})
            if not Employer.objects.filter(id=data['employer']):
                return Response({"status":"failed","response_code":status.HTTP_404_NOT_FOUND,"message":"sorry, employee does not exist"})
                
            seralizer = EmployeeSerializer(data=request.data)
            if seralizer.is_valid():
                seralizer.save()
                return Response({"status":"success","response_code":status.HTTP_201_CREATED,"message":"Employee created successfully"})
                # return Response(seralizer.data,status=status.HTTP_201_CREATED)
            return Response(seralizer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":"success","response_code":status.HTTP_201_CREATED,"message":"Employee created successfully"})
            
    

class EmployeesDetailsAPi(APIView):
     
    def get(self,request,pk):
        try:
            Employees = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({"error":"employee not fount"},status=404)
        seralizer = EmployeeSerializer(Employee,many=True)
        return Response(seralizer.data)
    
    
    def put(self,request,pk):
        try:
            Employees = Employee.objects.get(pk=pk)    
        except Employee.DoesNotExist:
            return Response({"error":"employee not found"},status=404)
        
        seralizers = EmployeeSerializer(Employee,data = request.data)
        if seralizers.is_valid():
            seralizers.save()
            return Response({"status":"success","Response_code":status.HTTP_201_CREATED,"message":"employee datas are updated"})
        return Response(seralizers.errors,status=400)
     
    def Delete(self,request,pk):
        try:
            Employees = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({"status":"failed","Response_code":status.HTTP_404_NOT_FOUND,"message":"delete is not working"})

        Employee.delete()
        return Response({"status":"deleted","response_code":status.HTTP_200_OK,"message":"emplyee deleted succefully"})