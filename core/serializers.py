from rest_framework import serializers
from .models import User, Contract

class ContractSerializer(serializers.ModelSerializer):
    """ First Contract Serializer : all fields for now """
    class Meta:
        model = Contract
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    """ First User Serializer : all fields for now """
    class Meta:
        model = User
        fields = '__all__'
