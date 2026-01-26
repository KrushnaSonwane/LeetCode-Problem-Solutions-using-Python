with tmp as (
    select product_id as id, sum(unit) as unit from Orders
where year(order_date) = '2020' and month(order_date) = '2'
group by product_id
)

select 
    a.product_name,
    b.unit
from Products a
join tmp b
on b.id = a.product_id
where b.unit >= 100