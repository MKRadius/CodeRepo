update game
set location = (
    select ident 
    from airport
    where name = "Nottingham Airport"
), co2_consumed = co2_consumed + 500
where screen_name = "Vesa";



delete from goal_reached;



delete from game;