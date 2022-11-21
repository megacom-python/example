from django.urls import path
from orders import views

urlpatterns = [
    path("orders/", views.OrderAPIView.as_view()),
    path("dishes/", views.DishAPIView.as_view()),
    path("calculator/", views.CalculatorAPIView.as_view()),
    path("list-orders/", views.ListOrdersAPIView.as_view()),
]
