create table mesure (id numeric, qd timestamp, val numeric);
insert into mesure values (1, now(), 23);
insert into mesure values (2, now()+interval '1 day', 223);
insert into mesure values (3, now()+interval '2 day', 253);
insert into mesure values (4, now()+interval '5 day', 227);
insert into mesure values (5, now()+interval '16 day', 34);

