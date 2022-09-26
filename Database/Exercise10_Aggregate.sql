select max(elevation_ft) as "max(elevation_ft)"
from airport;



select continent, count(*)
from country
group by continent;



select screen_name, count(*)
from game, goal_reached
where id = game_id
group by screen_name;