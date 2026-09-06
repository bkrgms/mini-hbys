insert into departments (name) values ('Kardiyoloji'),('Ortopedi'),('Dahiliye');

insert into doctors (full_name, department_id) values
('Dr. Ayşe Yilmaz', 1),
('Dr. Mehmet Yilmaz', 2),
('Dr. Mehmet Demir', 1);

insert into patients (full_name, birth_date, gender) values
('Ali Zengin','1990-05-12','male'),
('Ayşe Fakir','2003-01-01','female');

insert into appointments (patient_id, doctor_id, appointment_date) values
(1,1,'2026-09-08'),
(2,2,'2026-10-09');	

select doctors.full_name, departments.name from departments
inner join doctors
	on doctors.department_id = departments.id;

select * from patients p where gender='male'

select count(*) as departments_count from departments d 
