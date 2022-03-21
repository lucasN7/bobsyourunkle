"""bobsyourunkle URL Configuration"""

from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from core.views import ContractRetUpdDesView , ContractListCreView, UserRetUpdDesView, UserListCreView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/contract/<number>/', ContractRetUpdDesView.as_view(), name='contract-ret-upd-des'),
    path('api/contract/', ContractListCreView.as_view(), name='contract-list-cre'),
    path('api/user/<username>/', UserRetUpdDesView.as_view(), name='user-ret-upd-des'),
    path('api/user/', UserListCreView.as_view(), name='user-list-cre'),
]
