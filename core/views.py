from rest_framework import status, generics, mixins
from .serializers import ContractSerializer, UserSerializer
from .models import Contract, User


class ContractListCreView(generics.ListCreateAPIView):
	""" ListCreateAPIView to manage Contracts"""
	serializer_class = ContractSerializer 
	queryset = Contract.objects.all()

class ContractRetUpdDesView(generics.RetrieveUpdateDestroyAPIView):
	""" RetrieveUpdateDestroyAPIView to manage Contracts"""
	serializer_class = ContractSerializer 
	queryset = Contract.objects.all()
	lookup_field = 'number'

class UserListCreView(generics.ListCreateAPIView):
	""" ListCreateAPIView to manage Users"""
	serializer_class = UserSerializer 
	queryset = User.objects.all()

class UserRetUpdDesView(generics.RetrieveUpdateDestroyAPIView):
	""" RetrieveUpdateDestroyAPIView to manage Users"""
	serializer_class = UserSerializer 
	queryset = User.objects.all()
	lookup_field = 'username'