# Write your MySQL query statement below
with tmp as (
    select 
        d.*,
        avg(
            case
                when month(t.trip_date) < 7 then t.distance_km / t.fuel_consumed
            end
        ) as first_half_avg,
        avg(
            case
                when month(t.trip_date) > 6 then t.distance_km / t.fuel_consumed
            end
        )as second_half_avg
    from drivers d
    left join trips t
    on t.driver_id = d.driver_id
    group by t.driver_id
)

select
    driver_id,
    driver_name,
    round(first_half_avg, 2) as first_half_avg,
    round(second_half_avg, 2) as second_half_avg,
    round(second_half_avg - first_half_avg, 2) as efficiency_improvement
from tmp
where 
    first_half_avg is not null and 
    second_half_avg is not null and 
    round(second_half_avg - first_half_avg, 2) > 0
order by 
    efficiency_improvement desc, driver_name