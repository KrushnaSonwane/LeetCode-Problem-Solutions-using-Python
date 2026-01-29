# Write your MySQL query statement below
with tmp as (
    select 
        *, count(num) as cnt
    from MyNumbers
    group by num
),
tmp2 as (select num from tmp where cnt = 1 order by num desc)
select max(num) as num from tmp2
