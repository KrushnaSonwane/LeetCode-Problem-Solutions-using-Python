# Write your MySQL query statement below
with tmp as (
    select
        customer_id,
        count(*) as total_orders,
        sum(
            case
                when time(order_timestamp) >= "11:00:00" and time(order_timestamp) <= "14:00:00" then 1
                when time(order_timestamp) >= "18:00:00" and time(order_timestamp) <= "21:00:00" then 1
                else 0
            end
        ) as peak_hour,
        round(avg(order_rating), 2) as order_rating,
        sum(
            case 
                when order_rating is not null then 1
                else 0 
            end
        ) as rated
    from restaurant_orders
    group by customer_id
)

select 
    customer_id,
    total_orders,
    round((peak_hour / total_orders) * 100, 0) as peak_hour_percentage,
    order_rating as average_rating
from tmp
where 
    total_orders > 2 and 
    ((peak_hour / total_orders) * 100 ) >= 60 and 
    order_rating >= 4 and 
    (total_orders / 2) <= rated
order by 
    order_rating desc, customer_id desc