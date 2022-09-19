/*1*/
select country.name as "country name", airport.name as "airport name"
from country
inner join airport 
on country.iso_country = airport.iso_country 
where airport.scheduled_service = "yes" and country.name = "Finland";


/*2*/
select game.screen_name as screen_name, airport.name as name
from game
inner join airport
on game.location = airport.ident;


/*3*/
select game.screen_name as screen_name, country.name as name
from airport
inner join country on airport.iso_country = country.iso_country
inner join game on airport.ident = game.location;


/*4*/
select airport.name as name, game.screen_name 
from airport 
left join game
on airport.ident = game.location
where airport.name like "%Hels%";


/*5*/
select goal.name as name, game.screen_name
from goal
join goal_reached on goal.id = goal_reached.goal_id
left join game on goal_reached.game_id = game.id;