/*1*/
select name
from country
where ident = (
    select name from airport
    from airport
    where name like "Satsuma%");