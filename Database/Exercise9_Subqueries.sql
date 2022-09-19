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


/*3*/
select screen_name
from game
where id = (
    select game_id
    from goal_reached
    where goal_id = (
        select name
        from goal
        where name = "CLOUDS"
    )
);


/*3*/