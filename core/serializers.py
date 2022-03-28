from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from datetime import date
from .models import User, Contract

class UserFullSerializer(serializers.ModelSerializer):
    """ First User Serializer : all fields for now """

    class Meta:
        model = User
        fields = ("id", "username", "password", "first_name", "last_name", "email", "is_staff",
                 "is_active", "date_joined",)
        
    def create(self, validated_data):
        # hash the password so it's not stored in plain
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)


class UserPartialSerializer(serializers.ModelSerializer):
    """ Partial serializer used to display limited User data """

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "date_joined",)

        
class ContractReadSerializer(serializers.ModelSerializer):
    """ Contract Read Serializer : display clients details """
    
    clients = UserPartialSerializer(many=True, read_only=True)
    class Meta:
        model = Contract
        fields = ("number", "start_dt", "end_dt", "cancel_dt", "created_dt", "created_by", 
                  "modified_dt", "modified_by", "clients", "status",)

        
class ContractWriteSerializer(serializers.ModelSerializer):
    """ Contract Write Serializer : Allow saving clients that exists """
    
    # using SlugRelatedField to allow admin user to save clients into contracts by username and 
    # existing users only!
    clients = serializers.SlugRelatedField(queryset=User.objects.all(),
                                           many=True, 
                                           slug_field='username',
                                           required=True)   
  
    class Meta:
        model = Contract
        fields = ("number", "start_dt", "end_dt", "cancel_dt", "created_dt", "created_by", 
                  "modified_dt", "modified_by", "clients",)



class ContractCancelSerializer(serializers.ModelSerializer):
    """ Contract Cancel Serializer : Update Cancel date """
    
    cancel_dt = serializers.DateField(required=True, allow_null=False)

    class Meta:
        model = Contract
        fields = ("number", "cancel_dt",)

    def validate(self, data):
        """
        Check that cancel is after today.
        """
        if data.get('cancel_dt') is None or data['cancel_dt'] < date.today():
            raise serializers.ValidationError("Cancel date needs to be today or later")
        return data

        