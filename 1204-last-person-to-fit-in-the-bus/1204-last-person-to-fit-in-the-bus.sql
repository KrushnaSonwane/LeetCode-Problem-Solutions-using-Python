# Write your MySQL query statement below
with tmp as (select person_name, sum_t from(
select q2.*,
    (select sum(q.weight) from Queue q where q2.turn >= q.turn) as sum_t
from Queue q2
order by q2.turn) tmp
where sum_t <= 1000)
select tt.person_name from (select t.*, row_number() over(order by t.sum_t desc) as rn
from tmp t) tt
where tt.rn = 1