# Write your MySQL query statement below
with tmp as (select 
    sell_date, 
    count(distinct product) as num_sold 
    from Activities 
    group by sell_date
),

res as (
    SELECT 
        a.sell_date, 
        t.num_sold, 
        GROUP_CONCAT(distinct product) as products
    FROM Activities a
    join tmp t
    on a.sell_date = t.sell_date
    group by a.sell_date
    order by a.product
)
select * 
from res 
order by sell_date;