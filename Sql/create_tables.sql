create table department(
id serial primary key,
name varchar(250) not null
);

create type cam_vector as enum ('enter', 'exit');
create type account_role as enum ('viewer', 'technical_engineer');
create type emp_status as enum ('working', 'trainees', 'vacation', 'dismissed');

create table employee(
id serial primary key,
first_name varchar(250) not null,
last_name varchar(250) not null,
status emp_status not null,
dept_id integer references department(id)
);

alter table department
add column cheif_id integer not null references employee(id);

create table biometrics(
id serial primary key,
original_image integer[][][] not null unique,
landmarks integer[][] not null,
features numeric[] not null unique,
emp_id integer not null references employee(id)
);

create table checkpoint(
id serial primary key,
address varchar not null
);

create table camera(
id serial primary key,
vector cam_vector not null,
device_name varchar not null unique,
ckpt_id integer not null references checkpoint(id)
);

create table visit(
id serial primary key,
date_time timestamp not null,
event varchar(500) not null,
emp_id integer not null references employee(id),
camera_id integer not null references camera(id)
);

create table account(
id serial primary key,
username varchar(100) not null unique,
password varchar(40) not null,
role account_role not null
)




