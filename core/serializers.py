from rest_framework import serializers
from .models import User, Contract

class ContractSerializer(serializers.ModelSerializer):
    """ First Contract Serializer : all fields for now """
    class Meta:
        model = Contract
        fields = ("number", "start_dt", "end_dt", "cancel_dt", "created_dt", "modified_dt",
                 "created_by", "modified_by", "clients", "status")

class UserSerializer(serializers.ModelSerializer):
    """ First User Serializer : all fields for now """
    class Meta:
        model = User
        fields = '__all__'
