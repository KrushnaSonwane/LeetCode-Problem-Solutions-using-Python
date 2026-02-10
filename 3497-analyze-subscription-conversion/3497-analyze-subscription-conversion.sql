# Write your MySQL query statement below
select * from(
select
    u.user_id,
    round(avg(
        case
            when u.activity_type = 'free_trial' then u.activity_duration
        end
    ), 2) as trial_avg_duration,
    round(avg(
        case
            when u.activity_type = 'paid' then u.activity_duration
        end
    ), 2) as paid_avg_duration 
from UserActivity u
group by u.user_id
) a
where paid_avg_duration is not null and trial_avg_duration is not null
order by user_id