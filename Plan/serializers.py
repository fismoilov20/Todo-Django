from .models import *

from rest_framework.serializers import ModelSerializer

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

