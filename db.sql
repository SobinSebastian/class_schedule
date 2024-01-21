/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 10.4.14-MariaDB : Database - class_shedule
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`class_shedule` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `class_shedule`;

/*Table structure for table `calender` */

DROP TABLE IF EXISTS `calender`;

CREATE TABLE `calender` (
  `calender_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`calender_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `calender` */

insert  into `calender`(`calender_id`,`date`,`title`,`description`) values 
(1,'2022-03-10','TITLE','DES'),
(3,'2022-03-14','DREG','A');

/*Table structure for table `classupdates` */

DROP TABLE IF EXISTS `classupdates`;

CREATE TABLE `classupdates` (
  `update_id` int(11) NOT NULL AUTO_INCREMENT,
  `schedule_id` int(11) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  `portions` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`update_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `classupdates` */

insert  into `classupdates`(`update_id`,`schedule_id`,`teacher_id`,`subject_id`,`portions`) values 
(1,1,2,2,'oop'),
(2,1,2,2,'control statements'),
(3,1,2,2,'conditional');

/*Table structure for table `courses` */

DROP TABLE IF EXISTS `courses`;

CREATE TABLE `courses` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `department_id` int(11) DEFAULT NULL,
  `course_name` varchar(50) DEFAULT NULL,
  `duration` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `courses` */

insert  into `courses`(`course_id`,`department_id`,`course_name`,`duration`,`description`) values 
(1,1,'d1c1','2','dfghj'),
(3,2,'d2c1','4','dcvgbh'),
(4,3,'d3c1','5','ertyu');

/*Table structure for table `departments` */

DROP TABLE IF EXISTS `departments`;

CREATE TABLE `departments` (
  `department_id` int(11) NOT NULL AUTO_INCREMENT,
  `department_name` varchar(50) DEFAULT NULL,
  `department_description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `departments` */

insert  into `departments`(`department_id`,`department_name`,`department_description`) values 
(2,'d2','uhgfd'),
(3,'d3','des'),
(5,'d1','5');

/*Table structure for table `doubts` */

DROP TABLE IF EXISTS `doubts`;

CREATE TABLE `doubts` (
  `doubt_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  `doubt` varchar(50) DEFAULT NULL,
  `answer` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`doubt_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `doubts` */

insert  into `doubts`(`doubt_id`,`student_id`,`subject_id`,`doubt`,`answer`) values 
(1,1,1,'HHHY','jj'),
(2,1,1,'dfhd','hlo'),
(3,1,2,'VvHf','Pending'),
(4,1,2,'Bsjts','Pending'),
(5,1,2,'Zfhzjxfuxtu','Pending'),
(6,1,1,'Guud','Pending');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'anuanu','anuanuanu','teacher'),
(4,'arun','arun','teacher'),
(5,'wells','wells','teacher'),
(13,'ss','ss','student'),
(15,'ddd','dddd','student'),
(16,'jorbin','jorbin','teacher');

/*Table structure for table `post_notes` */

DROP TABLE IF EXISTS `post_notes`;

CREATE TABLE `post_notes` (
  `note_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_id` int(11) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  `note` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`note_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `post_notes` */

insert  into `post_notes`(`note_id`,`subject_id`,`teacher_id`,`note`) values 
(1,1,2,'static/6922b677-2bbc-4030-b0cd-f39c9450508bCapture.PNG'),
(2,1,2,'static/e3ee406d-5b37-4e24-96da-e01794761bddCapture.PNG'),
(3,1,2,'static/e4f9c74f-aed6-48b0-9a45-8cea9ac0be92currency.jpg'),
(4,1,2,'static/89b3f2d7-3896-4291-a821-fc5036745cf4admin_view_customer.PNG'),
(5,4,3,'static/6266c90f-b19f-4fd1-a853-b8c2c70c8422att.png');

/*Table structure for table `schedule` */

DROP TABLE IF EXISTS `schedule`;

CREATE TABLE `schedule` (
  `schedule_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_id` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `starting_hour` varchar(50) DEFAULT NULL,
  `ending_hour` varchar(50) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  `teacher_availability_status` varchar(50) DEFAULT NULL,
  `schedule_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`schedule_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `schedule` */

insert  into `schedule`(`schedule_id`,`subject_id`,`date`,`starting_hour`,`ending_hour`,`teacher_id`,`teacher_availability_status`,`schedule_status`) values 
(1,2,'2022-03-08','13:02','14:00',2,'available','conducted'),
(2,1,'2022-03-02','14:02','15:03',1,'pending','pending'),
(3,1,'2022-03-03','13:00','14:00',1,'pending','pending'),
(6,4,'2022-03-18','08:33','04:06',3,'available','conducted');

/*Table structure for table `students` */

DROP TABLE IF EXISTS `students`;

CREATE TABLE `students` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `house_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `pincode` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `students` */

insert  into `students`(`student_id`,`login_id`,`course_id`,`first_name`,`last_name`,`house_name`,`place`,`phone`,`pincode`,`email`,`gender`,`dob`) values 
(1,13,3,'stervi','kj','dfrh','fh','hfhfhf','fhfhf','9876546543','Male','2022-03-01');

/*Table structure for table `subjects` */

DROP TABLE IF EXISTS `subjects`;

CREATE TABLE `subjects` (
  `subject_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_id` int(11) DEFAULT NULL,
  `subject_name` varchar(50) DEFAULT NULL,
  `total_hours` varchar(50) DEFAULT NULL,
  `subject_description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`subject_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `subjects` */

insert  into `subjects`(`subject_id`,`course_id`,`subject_name`,`total_hours`,`subject_description`) values 
(1,3,'d2c1s1','6','qwer'),
(2,3,'d2c1s2','7','sr'),
(4,4,'d1c1s1','8','fcghf'),
(5,4,'tax','2','sdrfguhjkm');

/*Table structure for table `teachers` */

DROP TABLE IF EXISTS `teachers`;

CREATE TABLE `teachers` (
  `teacher_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `teachers` */

insert  into `teachers`(`teacher_id`,`login_id`,`department_id`,`subject_id`,`first_name`,`last_name`,`phone`,`email`,`qualification`) values 
(1,4,2,1,'arun','arun','9876546543','a@gmail.com','pg'),
(2,5,2,2,'wells','wells','9876546543','a@gmail.com','MSC'),
(3,16,3,4,'jorbin','kj','9876546543','wells@gmail.com','45');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
