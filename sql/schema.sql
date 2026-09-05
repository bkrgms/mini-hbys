create table departments(
	id serial primary key,
	name varchar(100)
);

create table doctors(
	id serial primary key,
	full_name varchar(100),
	department_id int references departments(id) 
);

create table patients(
	id serial primary key,
	full_name varchar(100),
	birth_date date,
	gender varchar(10) check (gender in ('male','female','other'))
);

create table appointments(
	id serial primary key,
	patient_id int references patients(id),
	doctor_id int references doctors(id),
	appointment_date date,
	status varchar(20) default 'scheduled'
);