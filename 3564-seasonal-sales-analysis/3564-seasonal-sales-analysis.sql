# Write your MySQL query statement below
with tmp as (
    select 
        *,
        (
            case
                when month(sale_date) >= 3 and 5 >= month(sale_date) then "Spring"
                when month(sale_date) >= 6 and 8 >= month(sale_date) then "Summer"
                when month(sale_date) >= 9 and 11 >= month(sale_date) then "Fall"
                else "Winter"
            end
        ) as season,
        price * quantity as total
    from sales
),

a as ( 
    select 
        t.season,
        p.category,
        sum(t.quantity) as total_quantity,
        sum(t.total) as total_revenue
    from tmp t
    left join products p
    on p.product_id = t.product_id
    group by season, p.category
)
select 
    season,
    category,
    total_quantity,
    total_revenue
from(
    select 
    *, 
    rank() over(
        partition by aa.season 
        order by 
            aa.total_quantity desc, 
            aa.total_revenue desc, 
            aa.category
    ) as rnk
    from a aa
) as aaa
where rnk = 1