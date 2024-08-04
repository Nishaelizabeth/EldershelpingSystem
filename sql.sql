/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - eldershelpingsystem
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`eldershelpingsystem` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `eldershelpingsystem`;

/*Table structure for table `caregiver` */

DROP TABLE IF EXISTS `caregiver`;

CREATE TABLE `caregiver` (
  `Caregiver_id` int(11) NOT NULL AUTO_INCREMENT,
  `Login_id` int(11) DEFAULT NULL,
  `Fname` varchar(255) DEFAULT NULL,
  `Lname` varchar(255) DEFAULT NULL,
  `Place` varchar(255) DEFAULT NULL,
  `Phone` varchar(15) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Caregiver_id`),
  KEY `Login_id` (`Login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `caregiver` */

insert  into `caregiver`(`Caregiver_id`,`Login_id`,`Fname`,`Lname`,`Place`,`Phone`,`Email`) values 
(1,2,'jùjú','sea','ekm','02345678904','kjsjdksa@gmail.com');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `Chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `Sender_id` int(11) DEFAULT NULL,
  `Receiver_id` int(11) DEFAULT NULL,
  `Message` varchar(100) DEFAULT NULL,
  `Date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Chat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`Chat_id`,`Sender_id`,`Receiver_id`,`Message`,`Date`) values 
(1,2,1,'good','2024-02-25'),
(2,2,1,'heel','2024-02-25'),
(3,1,2,'hello','2024-02-05');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `Complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_id` int(11) DEFAULT NULL,
  `Complaint` varchar(100) DEFAULT NULL,
  `Reply` varchar(100) DEFAULT NULL,
  `Date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Complaint_id`),
  KEY `User_id` (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`Complaint_id`,`User_id`,`Complaint`,`Reply`,`Date`) values 
(1,1,'GOOD','yes','12-3-19');

/*Table structure for table `ecomplaints` */

DROP TABLE IF EXISTS `ecomplaints`;

CREATE TABLE `ecomplaints` (
  `Ecomplaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `Request_id` int(11) DEFAULT NULL,
  `Complaint` varchar(100) DEFAULT NULL,
  `Reply` varchar(100) DEFAULT NULL,
  `Date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Ecomplaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `ecomplaints` */

insert  into `ecomplaints`(`Ecomplaint_id`,`Request_id`,`Complaint`,`Reply`,`Date`) values 
(1,1,'bad','oh','21-3-13');

/*Table structure for table `ework` */

DROP TABLE IF EXISTS `ework`;

CREATE TABLE `ework` (
  `Ework_id` int(11) NOT NULL AUTO_INCREMENT,
  `Request_id` int(11) DEFAULT NULL,
  `Works` varchar(100) DEFAULT NULL,
  `Extraamount` varchar(100) DEFAULT NULL,
  `Status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Ework_id`),
  KEY `Request_id` (`Request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `ework` */

insert  into `ework`(`Ework_id`,`Request_id`,`Works`,`Extraamount`,`Status`) values 
(1,1,'worlss','500','pending'),
(2,1,'Red cotton Salwar With Red and blue mixed shawl','1000','pending'),
(3,1,'dfghjk','100','pending');

/*Table structure for table `info` */

DROP TABLE IF EXISTS `info`;

CREATE TABLE `info` (
  `Info_id` int(11) NOT NULL AUTO_INCREMENT,
  `Request_id` int(11) DEFAULT NULL,
  `Info` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Info_id`),
  KEY `Request_id` (`Request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `info` */

insert  into `info`(`Info_id`,`Request_id`,`Info`) values 
(1,1,'hjgjhhj hgjhgj hghgkj hghgkj ');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `Login_id` int(11) NOT NULL AUTO_INCREMENT,
  `Username` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Usertype` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`Login_id`,`Username`,`Password`,`Usertype`) values 
(1,'admin','admin','admin'),
(2,'hai','hai','caregiver'),
(3,'user','user','user');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `Payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `Request_id` int(11) DEFAULT NULL,
  `Amount` varchar(100) DEFAULT NULL,
  `Date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Payment_id`),
  KEY `Request_id` (`Request_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `Rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `Request_id` int(11) DEFAULT NULL,
  `Rated` int(11) DEFAULT NULL,
  `Review` varchar(100) DEFAULT NULL,
  `Date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Rating_id`),
  KEY `Request_id` (`Request_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `Request_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_id` int(11) DEFAULT NULL,
  `Wdetails_id` int(11) DEFAULT NULL,
  `Details` varchar(100) DEFAULT NULL,
  `Date` varchar(100) DEFAULT NULL,
  `Time` varchar(100) DEFAULT NULL,
  `Total` varchar(100) DEFAULT NULL,
  `Status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Request_id`),
  KEY `User_id` (`User_id`),
  KEY `Wdetails_id` (`Wdetails_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`Request_id`,`User_id`,`Wdetails_id`,`Details`,`Date`,`Time`,`Total`,`Status`) values 
(1,1,1,'dfsdgs','12-21-12','12.34','5000','Accepted');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `User_id` int(11) NOT NULL AUTO_INCREMENT,
  `Login_id` int(11) DEFAULT NULL,
  `Fname` varchar(100) DEFAULT NULL,
  `Lname` varchar(100) DEFAULT NULL,
  `Place` varchar(100) DEFAULT NULL,
  `Phone` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`User_id`),
  KEY `Login_id` (`Login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`User_id`,`Login_id`,`Fname`,`Lname`,`Place`,`Phone`,`Email`) values 
(1,3,'hai','hello','ekm','763978','jhjds@gmail.com');

/*Table structure for table `wdetails` */

DROP TABLE IF EXISTS `wdetails`;

CREATE TABLE `wdetails` (
  `Wdetails_id` int(11) NOT NULL AUTO_INCREMENT,
  `Caregiver_id` int(11) DEFAULT NULL,
  `Details` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Wdetails_id`),
  KEY `Caregiver_id` (`Caregiver_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `wdetails` */

insert  into `wdetails`(`Wdetails_id`,`Caregiver_id`,`Details`,`amount`) values 
(1,1,'dfdsfs','500'),
(2,1,'Red cotton Salwar With Red and blue mixed shawl','5001');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
