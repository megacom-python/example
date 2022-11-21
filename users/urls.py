from django.urls import path
from users import views

urlpatterns = [
    path("users/", views.UsersListAPIView.as_view()),
    path("register-user/", views.RegisterUserAPIView.as_view()),
    path("obtain-token/", views.ObtainTokenAPIView.as_view()),
]
