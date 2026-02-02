# Write your MySQL query statement below
select 
    tt.id,
    case
        when tt.p_id is null then "Root"
        when (select count(*) from Tree t where t.p_id = tt.id) = 0 then "Leaf"
        else "Inner"
    end as type
from Tree tt