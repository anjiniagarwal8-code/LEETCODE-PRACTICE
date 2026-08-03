# Write your MySQL query statement below
with dailyamount as (select visited_on,sum(amount) as amount from customer group by visited_on) 
select a.visited_on,sum(b.amount) as amount ,round(avg(b.amount), 2) as average_amount from dailyamount a join dailyamount b on datediff(a.visited_on, b.visited_on) between 0 and 6 where a.visited_on >=(select date_add(min(visited_on),interval 6 day) from customer)
group by a.visited_on order by a.visited_on asc;
