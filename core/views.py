from django.http import HttpResponseForbidden
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework import status, generics, mixins
from .serializers import ContractReadSerializer, ContractWriteSerializer, UserFullSerializer, \
	UserPartialSerializer, ContractCancelSerializer
from .models import Contract, User
from .utils import FullPartialSerializerMixin
from .permissions import IsOwnerOrAdmin


""" Notes:
1. Default permissions (from settings is @permission_classes([IsOwnerOrAdmin]))
2. I liked in the past using the generics and mixins because of their powerful out of the box 
features like filters that we usually need down the line
3. Playing with dual serializer class to allow/return different set of data depending 
on the request method. Not sure how much you guys like this, keen for feedback!
"""

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

class ContractListCreateView(FullPartialSerializerMixin, generics.ListCreateAPIView):
	""" List/Create APIView to manage Contracts"""
	full_serializer_class = ContractReadSerializer
	partial_serializer_class = ContractWriteSerializer
	
	def get_queryset(self):
		if not self.request.user.is_staff:
			return self.request.user.contracts
		return Contract.objects.all()

	def get(self, request, *args, **kwargs):
		self.partial = False
		return super().get(request, *args, **kwargs)
	
	def post(self, request, *args, **kwargs):
		self.partial = True
		return super().post(request, *args, **kwargs)

	
class ContractRetUpdDesView(FullPartialSerializerMixin, generics.RetrieveUpdateDestroyAPIView):
	""" RetrieveUpdateDestroy APIView to manage Contracts"""
	full_serializer_class = ContractReadSerializer
	partial_serializer_class = ContractWriteSerializer
	queryset = Contract.objects.all()
	lookup_field = 'number'
	
	def get(self, request, *args, **kwargs):
		self.partial = False
		return super().get(request, *args, **kwargs)
	
	def post(self, request, *args, **kwargs):
		self.partial = True
		return super().post(request, *args, **kwargs)
	
	def patch(self, request, *args, **kwargs):
		# do not allow User to fully modify their contract (PATCH are allowed for cancellation)
		if not self.request.user.is_staff:
			return HttpResponseForbidden
		self.partial = True
		return super().patch(request, *args, **kwargs)


class ContractCancelView(generics.UpdateAPIView):
	""" UpdateAPIView to cancel contracts """
	serializer_class = ContractCancelSerializer
	queryset = Contract.objects.all()
	lookup_field = 'number'
	
