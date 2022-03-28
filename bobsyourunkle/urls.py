"""bobsyourunkle URL Configuration"""

from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from core.views import ContractRetUpdDesView , ContractListCreateView, UserRetrieveDestroyView, \
    UserListCreateView, ContractCancelView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/contract/<number>/', ContractRetUpdDesView.as_view(), name='contract-ret-upd-des'),
    path('api/contract/', ContractListCreateView.as_view(), name='contract-list-cre'),
    path('api/contractcancel/<number>/', ContractCancelView.as_view(), name='contract-ret-upd-des'),
    path('api/user/<username>/', UserRetrieveDestroyView.as_view(), name='user-ret-upd-des'),
    path('api/user/', UserListCreateView.as_view(), name='user-list-cre'),
]
