select max(elevation_ft) as "max(elevation_ft)"
from airport;



select continent, count(*)
from country
group by continent;



select screen_name, count(*)
from game, goal_reached
where game.id = game.game_id
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



select name
from country
where iso_country in (
    select iso_country
    from airport
    where elevation_ft in (
        select max(elevation_ft)
        from airport
    )
);



select count(*)
from game, goal_reached
where game.id = goal_reached.game_id and screen_name = "Vesa";



select name
from airport
where latitude_deg in (
    select min(latitude_deg)
    from airport
);