from django.utils.translation import gettext_lazy as _
from django.db import models


class Order(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    # @property
    # def total_sum(self):
    #     result: int = 0
    #     ordered_set: models.QuerySet["DishInOrder"] = self.dishes.all()
    #     for ordered in ordered_set:
    #         result += ordered.dish.price
    #     return result


class Dish(models.Model):
    title = models.CharField(_("Название"), max_length=100)
    price = models.PositiveIntegerField(_("Цена"))


class DishInOrder(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="dishes"
    )
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
