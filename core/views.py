from django.http import HttpResponseForbidden
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework import status, generics, mixins
from .serializers import ContractSerializer, UserFullSerializer, UserPartialSerializer
from .models import Contract, User
from .utils import FullPartialSerializerMixin
from .permissions import IsOwnerOrAdmin


""" Notes:
1. Default permissions (from settings is @permission_classes([IsOwnerOrAdmin]))
2. I liked in the past using the generics and mixins because of their powerful out of the box 
features like filters that we usually need down the line
"""

class ContractListCreateView(generics.ListCreateAPIView):
	""" List/Create APIView to manage Contracts"""
	serializer_class = ContractSerializer 
	
	def get_queryset(self):
		if not self.request.user.is_staff:
			return self.request.user.contracts
		return Contract.objects.all()

	def post(self, request, *args, **kwargs):
		return super().post(request, *args, **kwargs)

	
class ContractRetUpdDesView(generics.RetrieveUpdateDestroyAPIView):
	""" RetrieveUpdateDestroy APIView to manage Contracts"""
	serializer_class = ContractSerializer 
	queryset = Contract.objects.all()
	lookup_field = 'number'

	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)
	
	def delete(self, request, *args, **kwargs):
		return
		return super().delete(request, *args, **kwargs)


# On this one, playing with dual serializer class to allow/return different set of data depending 
# on the request method. Not sure how much you guys like this, keen for feedback!
@permission_classes([IsAdminUser])
class UserListCreateView(FullPartialSerializerMixin, generics.ListCreateAPIView):
	""" ListCreateAPIView to manage Users"""
	partial = False
	queryset = User.objects.all()
	full_serializer_class = UserFullSerializer
	partial_serializer_class = UserPartialSerializer
	
	def get(self, request, *args, **kwargs):
		self.partial = True
		return super().get(request, *args, **kwargs)
	
	def post(self, request, *args, **kwargs):
		self.partial = False
		return super().post(request, *args, **kwargs)

	
class UserRetrieveDestroyView(mixins.DestroyModelMixin, generics.RetrieveAPIView):
	""" Retrieve/Destroy APIView to manage Users"""
	queryset = User.objects.all()
	lookup_field = 'username'
	serializer_class = UserFullSerializer