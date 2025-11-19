from rest_framework import serializers
from .models import Employer, Employee

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'
        
    def validate_phone(self,value):
        
        if not value:
            raise Exception("phone number is reqired!")
            # raise serializers.ValidationError("Phone number is required!")
        
        if not value.isdigit():
           # raise Exception("Phone number must contain digits only")
            raise serializers.ValidationError("Phone number must contain digits only")

        
        if len(value)<10 or len(value)>15:
            # return Exception("Phone number must be between 10 and 15 digits")
            raise serializers.ValidationError("Phone number must be between 10 and 15 digits")

        return value

    def validate_name(self, value):
        if not value:
            raise Exception("name is reqired!")
        return value
            # raise serializers.ValidationError("name is required!")
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        
    def validation_employer(self, data):
        if not Employer.objects.filter(id=data):
            raise Exception('sorry, employee does not exist')
        return data
