with tmp as (select 
    a.visited_on,
    sum(a.sm) over(
        order by a.visited_on 
        rows between 6 preceding and current row
    ) as amount,
    round(avg(a.sm) over(
        order by a.visited_on 
        rows between 6 preceding and current row
    ), 2) as average_amount,
    row_number() over(order by a.visited_on) as rn
from
(select
    c.visited_on,
    sum(c.amount) as sm
from Customer c
group by c.visited_on
) a
)
select visited_on, amount, average_amount from tmp where rn > 6