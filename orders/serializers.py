from typing import Any, Dict
from rest_framework import serializers
from .models import DishInOrder, Order, Dish
from users.serializers import UserSerializer
from django.db.models import QuerySet


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"


class DishInOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishInOrder
        fields = ("id", "dish", "quantity")


class OrderSerializer(serializers.ModelSerializer):
    dishes = DishInOrderSerializer(many=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data: Dict[str, Any]):
        """
        {
            "dishes": [
                {
                    "dish": 1,
                    "quantity": 2
                },
                {
                    "dish": 2,
                    "quantity": 1
                }
            ]
        }


        1. Browser -> Server (HTTP)
            http://ip:port/orders/

            JSON {
                ...
            }

        2. urls.py -> views.py

        ? request

        3. views.py (POST) -> serializers.py
        """
        user = self.context.get("request").user
        instance = Order.objects.create(user=user)
        dishes_data = validated_data.pop("dishes")
        for dish_data in dishes_data:
            DishInOrder.objects.create(order=instance, **dish_data)
        return instance


class CalculatorSerializer(serializers.Serializer):
    operation = serializers.CharField(write_only=True)
    a = serializers.IntegerField(write_only=True)
    b = serializers.IntegerField(write_only=True)
    result = serializers.IntegerField(read_only=True)

    def create(self, validated_data: Dict[str, Any]):
        # print(f"{validated_data = }")
        operations = {"add": lambda a, b: a + b}
        return {
            "result": operations.get(validated_data["operation"])(
                validated_data.get("a"), validated_data.get("b")
            )
        }


class ListOrderSerializer(serializers.ModelSerializer):
    total_sum = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ("id", "user", "total_sum")

    # def get_total_sum(self, obj: Order):
    #     result: int = 0
    #     ordered_set: QuerySet["DishInOrder"] = obj.dishes.all()
    #     for ordered in ordered_set:
    #         result += ordered.dish.price
    #     return result
