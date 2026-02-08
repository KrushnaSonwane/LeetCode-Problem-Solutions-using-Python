# Write your MySQL query statement below

select 
    distinct s.product_id,
    p.product_name
from Product p
left join Sales s
on s.product_id = p.product_id
where s.product_id not in (
    select product_id from sales where sale_date > "2019-03-31" or sale_date < "2019-01-01"
)