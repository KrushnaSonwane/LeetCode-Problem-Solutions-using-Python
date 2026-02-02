# Write your MySQL query statement below
select 
    t.id,
    case
        when t.p_id is null then "Root"
        when (select count(*) from Tree where p_id = t.id) = 0 then "Leaf"
        else "Inner"
    end as type
from Tree t