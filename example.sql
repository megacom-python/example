SELECT orders_order.id
    , SUM(dish.price) AS total_sum
FROM orders_order AS order
JOIN orders_dishinorder AS ordered_dishes
    ON ordered_dishes.order_id = order.id
JOIN orders_dish AS dish
    ON dish.id = ordered_dishes.dish_id
GROUP BY order.id;