select max(elevation_ft) as "max(elevation_ft)"
from airport;



select continent, count(*)
from country
group by continent;



select screen_name, count(*)
from game, goal_reached
where id = game_id
group by screen_name;



select screen_name
from game
where co2_consumed in (
    select min(co2_consumed)
    from game
);



select country.name, count(*)
from country, airport
where country.iso_country = airport.iso_country
group by country.iso_country
order by count(*) desc
limit 50;



select country.name
from country, airport
where country.iso_country = airport.iso_country 
group by airport.iso_country
having count(airport.iso_country) >= 1000;



select name
from airport
where elevation_ft in (
    select max(elevation_ft)
    from airport
);