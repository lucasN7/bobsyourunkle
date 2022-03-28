"""core URL Configuration"""

from django.urls import path
from core.views import ContractRetUpdDesView , ContractListCreateView, UserRetrieveDestroyView, \
    UserListCreateView, ContractCancelView, ContractOptionCreateView, ContractOptionListView

# splitting core urls for better separation
urlpatterns = [
    path('contract/<number>/', ContractRetUpdDesView.as_view(), name='contract-ret-upd-des'),
    path('contract/', ContractListCreateView.as_view(), name='contract-list-cre'),
    path('contractcancel/<number>/', ContractCancelView.as_view(), name='contract-cancel'),
    path('user/<username>/', UserRetrieveDestroyView.as_view(), name='user-ret-upd-des'),
    path('user/', UserListCreateView.as_view(), name='user-list-cre'),
    path('contractoption-list/', ContractOptionListView.as_view(), name='option-list'),
    path('contractoption/', ContractOptionCreateView.as_view(), name='option-cre'),
]

