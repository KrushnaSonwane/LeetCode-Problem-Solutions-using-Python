# Write your MySQL query statement below
with tmp as (
select m.user_id, count(*) as cn, u.name as results
from MovieRating m
inner join Users u
on u.user_id = m.user_id
group by user_id
order by cn desc, u.name
limit 1),

tmp2 as (select mr.movie_id, avg(mr.rating) as aa, m.title as results
from MovieRating mr
inner join Movies m
on mr.movie_id = m.movie_id
where year(created_at) = 2020 and month(created_at) = 02
group by mr.movie_id
order by aa desc, results
limit 1)

select results from tmp
union all
select results from tmp2