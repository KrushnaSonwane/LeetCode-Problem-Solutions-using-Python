# Write your MySQL query statement below
with tmp as (
    select 
        s.user_id, 
        sum(
            case
                when action = "confirmed" then 1
                else 0
            end
        ) as confirmed,
        sum(
            case
                when action is not null then 1
                else 0
            end
        ) as total_counts
    from Signups s
    left join Confirmations c
    on s.user_id = c.user_id
    group by user_id
)
select 
    user_id,
    round(
        case
            when total_counts = 0 then 0
            else confirmed / total_counts
        end
    , 2) as confirmation_rate
from tmp