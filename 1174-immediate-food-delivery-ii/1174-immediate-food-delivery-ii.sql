# Write your MySQL query statement below
with tmp as(select
    customer_id as id, order_date as curr, customer_pref_delivery_date as nxt
from Delivery
order by order_date
),
tmp2 as (
    select *,
        row_number() over(partition by id order by curr) as rnk
    from tmp
)
select 
    round((count(*) / (
        select 
            count(distinct a.id) 
        from tmp2 a
    ) * 100), 2) as immediate_percentage from tmp2
where curr = nxt and rnk = 1