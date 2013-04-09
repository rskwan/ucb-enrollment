drop table if exists courses;
create table courses (
  id integer primary key autoincrement,
  title text not null
);

drop table if exists enrinfo;
create table enrinfo (
  id integer not null,
  date text not null,
  seatlimit integer not null,
  enrolled integer not null,
  waitlist integer not null,
  foreign key (id) references courses(id)
);