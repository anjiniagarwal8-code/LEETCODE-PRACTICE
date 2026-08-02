# Write your MySQL query statement below
select person_name from(select person_name,sum(weight) over (order by turn asc) as total_weight from queue ) as running_total where total_weight <= 1000 order by total_weight desc limit 1;

