# Write your MySQL query statement below
SELECT  ROUND(AVG(order_date = customer_pref_delivery_date) * 100, 2) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (SELECT customer_id, MIN(order_date) AS first_order_date FROM Delivery GROUP BY 1)

# (customer_id, order_date) 一定要加小括號
# 竟然可以直接在AVG裡面下條件：AVG(order_date = customer_pref_delivery_date) * 100