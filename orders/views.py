from rest_framework import generics
from .models import Order, DishInOrder, Dish
from .serializers import (
    ListOrderSerializer,
    OrderSerializer,
    DishInOrderSerializer,
    DishSerializer,
    CalculatorSerializer,
)
from django.db.models import QuerySet, Sum

from rest_framework.permissions import IsAuthenticated


class OrderAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class DishInOrderAPIView(generics.CreateAPIView):
    queryset = DishInOrder.objects.all()
    serializer_class = DishInOrderSerializer()


class DishAPIView(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class CalculatorAPIView(generics.CreateAPIView):
    serializer_class = CalculatorSerializer


class ListOrdersAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = ListOrderSerializer

    def get_queryset(self):
        qs: QuerySet[Order] = super().get_queryset()
        return qs.annotate(total_sum=Sum("dishes__dish__price"))
