###1

#select country.name as "country name", airport.name as "airport name" 
#from airport 
#inner join country ON airport.iso_country = country.iso_country 
#where country.name = "Iceland";

select country.name as "country name", airport.name as "airport name" 
from airport, country 
where airport.iso_country = country.iso_country and country.name = "Iceland";


###2
select airport.name as "airport name" 
from airport, country 
where airport.iso_country = country.iso_country 
    and country.name = "France" 
    and airport.type = "large_airport";


###3
select country.name as "country_name", airport.name as "airport_name"
from airport, country
where airport.iso_country = country.iso_country and country.continent = "AN";


###4
select airport.elevation_ft
from airport, game
where airport.ident = game.location and game.screen_name = "Heini";


###5
select (airport.elevation_ft * 0.3048) as elevation_m
from airport, game
where airport.ident = game.location and game.screen_name = "Heini";


###6
select airport.name as name
from airport, game
where airport.ident = game.location and game.screen_name = "Ilkka";


###7
select country.name as name
from airport, country, game
where airport.ident = game.location 
    and airport.iso_country = country.iso_country 
    and game.screen_name = "Ilkka";


###8
select goal.name
from game, goal, goal_reached
where game.id = goal_reached.game_id 
    and goal.id = goal_reached.goal_id 
    and game.screen_name = "Heini";



###9
select airport.name
from game, goal, goal_reached, airport
where game.id = goal_reached.game_id 
    and goal.id = goal_reached.goal_id 
    and game.location = airport.ident 
    and game.screen_name = "Ilkka" 
    and goal.name = "CLOUDS";



###10
select country.name as name
from game, goal, goal_reached, airport, country
where game.id = goal_reached.game_id 
    and goal.id = goal_reached.goal_id 
    and game.location = airport.ident 
    and airport.iso_country = country.iso_country
    and game.screen_name = "Ilkka" 
    and goal.name = "CLOUDS";