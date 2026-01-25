-- with tmp as (
select 
    e.name, b.bonus 
from employee e
left join Bonus b
on e.empId = b.empId
where b.bonus < 1000 or b.bonus is null

-- select 
--     name, 
--     bonus 
-- from tmp 
-- where bonus < 1000 or bonus is null