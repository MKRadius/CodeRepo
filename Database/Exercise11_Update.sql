update game
set screen_name = "Vesa"
where location in (
    select ident 
    from airport
    where name = "Nottingham Airport"
);



