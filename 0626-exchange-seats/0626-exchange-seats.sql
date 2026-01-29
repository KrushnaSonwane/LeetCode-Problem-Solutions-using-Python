# Write your MySQL query statement below
select  
    id,
    case
        when id % 2 = 0 then lag(student) over()
        else 
            case
                when lead(student) over() is null then student
                else lead(student) over()
            end
    end as student
from Seat