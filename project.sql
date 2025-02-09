show databases;
create database studentmanagement;
use studentmanagement;
create table details(studentname varchar(30),
rollno varchar(10) primary key,
course varchar(30),
semester varchar(20),
gender varchar(20),
contact varchar (20),
dob varchar (20),
fathername varchar(30),
address varchar (30)
);
insert into details values('abc','101','bca','v','male','1234567890',
'12 dec 2001','abc','xyz');
select * from details;
alter table details 
modify column contact varchar(15) check(length(contact)>=10);