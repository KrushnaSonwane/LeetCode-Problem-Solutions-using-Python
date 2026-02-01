with tmp as (SELECT
    customer_id,
    MIN(transaction_date) AS f_date,
    MAX(transaction_date) AS l_date,
    count(*) as p_count, SUM(case when transaction_type = "refund" then 1 else 0 end) as r_count
FROM customer_transactions
GROUP BY customer_id
)
select customer_id from tmp
where datediff(l_date, f_date) > 29 and (r_count / p_count) < 0.2 and p_count > 2
order by customer_id