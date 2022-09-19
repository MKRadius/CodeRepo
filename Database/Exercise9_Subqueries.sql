/*1*/
select name
from country
where iso_country = (
    select iso_country
    from airport
    where name like "Satsuma%"
);


/*2*/
select name 
from airport
where iso_country = (
    select iso_country
    from country
    where name = "Monaco"
);