from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User, Contract

class ContractSerializer(serializers.ModelSerializer):
    """ First Contract Serializer : all fields for now """

    class Meta:
        model = Contract
        fields = ("number", "start_dt", "end_dt", "cancel_dt", "created_dt", "modified_dt",
                 "created_by", "modified_by", "clients", "status",)
        
class UserFullSerializer(serializers.ModelSerializer):
    """ First User Serializer : all fields for now """

    class Meta:
        model = User
        fields = ("id", "username", "password", "first_name", "last_name", "email", "is_staff",
                 "is_active", "date_joined",)
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

class UserPartialSerializer(serializers.ModelSerializer):
    """ First User Serializer : all fields for now """

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "is_staff", "is_active", 
                  "date_joined",)

    # adding this so the password is hashed in the db (not in clear)
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)