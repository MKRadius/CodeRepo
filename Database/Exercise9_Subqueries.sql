/*1*/
select name
from country
where iso_country = (
    select iso_country
    from airport
    where name like "Satsuma%");