drop table if exists courses;
create table courses (
  ccn integer primary key,
  title text not null
);

drop table if exists enrinfo;
create table enrinfo (
  ccn integer not null,
  date text not null,
  seatlimit integer not null,
  enrolled integer not null,
  waitlist integer not null
);