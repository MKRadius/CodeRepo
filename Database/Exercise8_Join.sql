/*1*/
select country.name as "country name", airport.name as "airport name"
from country
inner join airport
where airport.scheduled_service = "yes" and country.name = "Finland";