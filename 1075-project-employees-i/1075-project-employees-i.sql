# Write your MySQL query statement below
select 
    project_id, 
    round(avg(experience_years),2) as average_years 
from (
    select 
        p.project_id, 
        e.experience_years
    from Project p
    left join Employee e
    on e.employee_id = p.employee_id
) tmp
group by tmp.project_id