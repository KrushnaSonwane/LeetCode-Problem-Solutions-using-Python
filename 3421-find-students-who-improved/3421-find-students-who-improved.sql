# Write your MySQL query statement below
with a as (select ss.* from(
select s.*,
    row_number() over(partition by s.student_id, s.subject order by s.exam_date) as rn
from Scores s) ss 
where ss.rn = 1),

b as (select ss.* from(
select s.*,
    row_number() over(partition by s.student_id, s.subject order by s.exam_date desc) as rn
from Scores s) ss 
where ss.rn = 1)

select a.student_id, a.subject, a.score as first_score, b.score as latest_score from a
inner join b
on a.student_id = b.student_id and b.subject = a.subject
where a.score < b.score