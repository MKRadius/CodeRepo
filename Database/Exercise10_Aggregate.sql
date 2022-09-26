select max(elevation_ft) as "max(elevation_ft)"
from airport;



select continent, count(name)
from country
group by continent;



select screen_name, count(*)
from game
having count(*) in (
    select game_id
    from goal_reached
);