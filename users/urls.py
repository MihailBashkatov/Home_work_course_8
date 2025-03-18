from django.urls import path

from users.apps import UsersConfig
from users.views import (PaymentsListAPIView, UserCreateAPIView,
                         UserDestroyAPIView, UserListAPIView,
                         UserPaymentsListAPIView, UserRetreiveAPIView,
                         UserUpdateAPIView)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
app_name = UsersConfig.name


urlpatterns = [
    path("user/create/", UserCreateAPIView.as_view(), name="user_create"),
    path("users/", UserListAPIView.as_view(), name="user_list"),
    path("user/<int:pk>/", UserRetreiveAPIView.as_view(), name="user_detail"),
    path("user/update/<int:pk>/", UserUpdateAPIView.as_view(), name="user_update"),
    path("user/delete/<int:pk>/", UserDestroyAPIView.as_view(), name="user_delete"),
    # Payment endpoints
    path("payments/", PaymentsListAPIView.as_view(), name="payments_list"),
    path(
        "user_payments/", UserPaymentsListAPIView.as_view(), name="user_payments_list"
    ),
    # Getting tokens endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
