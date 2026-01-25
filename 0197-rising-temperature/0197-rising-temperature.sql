# Write your MySQL query statement below
with tmp as (
    select
        id,
        recordDate as cur,
        temperature,
        lag(temperature) over(order by recordDate) as pre,
        lag(recordDate) over() as preD
    from Weather
    -- order by temperature
)
select 
    id
from tmp
where pre < temperature and (preD + interval 1 day) = cur