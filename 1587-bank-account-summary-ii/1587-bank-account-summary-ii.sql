with t as (
    select 
        account,
        sum(amount) as balance
    from Transactions
    group by account
)
-- select * from t
select 
    u.name, t.balance
    from Users u
    join  t
    on t.account = u.account
where t.balance > 10000
