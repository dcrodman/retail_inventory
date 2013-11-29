CREATE DATABASE  IF NOT EXISTS `retail-inventory` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `retail-inventory`;
-- MySQL dump 10.13  Distrib 5.6.13, for osx10.6 (i386)
--
-- Host: 127.0.0.1    Database: retail-inventory
-- ------------------------------------------------------
-- Server version	5.6.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Temporary table structure for view `contact_info`
--

DROP TABLE IF EXISTS `contact_info`;
/*!50001 DROP VIEW IF EXISTS `contact_info`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `contact_info` (
  `phone` tinyint NOT NULL,
  `email` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `contacts`
--

DROP TABLE IF EXISTS `contacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contacts` (
  `address` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `city` varchar(45) NOT NULL,
  `state` varchar(2) NOT NULL,
  PRIMARY KEY (`address`),
  UNIQUE KEY `address` (`address`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts`
--

LOCK TABLES `contacts` WRITE;
/*!40000 ALTER TABLE `contacts` DISABLE KEYS */;
INSERT INTO `contacts` VALUES ('34B Mary St','dcrodman@gmail.com','4102366777','Charleston','SC');
/*!40000 ALTER TABLE `contacts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customers` (
  `name` varchar(255) NOT NULL,
  `contact` varchar(255) NOT NULL DEFAULT '',
  `customer_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`customer_id`,`name`,`contact`),
  UNIQUE KEY `customer_id_UNIQUE` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES ('Random Guy','1',1);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_shifts`
--

DROP TABLE IF EXISTS `employee_shifts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee_shifts` (
  `employee_id` int(11) NOT NULL,
  `date` date NOT NULL DEFAULT '0000-00-00',
  `start_time` varchar(7) DEFAULT NULL,
  `end_time` varchar(7) DEFAULT NULL,
  PRIMARY KEY (`employee_id`,`date`),
  CONSTRAINT `employee_shifts_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_shifts`
--

LOCK TABLES `employee_shifts` WRITE;
/*!40000 ALTER TABLE `employee_shifts` DISABLE KEYS */;
INSERT INTO `employee_shifts` VALUES (1,'0000-00-00','4:00pm','9:00pm'),(1,'2013-11-28','9:00 AM','8:00 AM'),(1,'2013-11-29','8:00 AM','8:00 AM'),(1,'2013-12-05','8:00 AM','8:00 AM'),(7,'2013-11-29','8:00 AM','8:00 AM');
/*!40000 ALTER TABLE `employee_shifts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `employeedetails`
--

DROP TABLE IF EXISTS `employeedetails`;
/*!50001 DROP VIEW IF EXISTS `employeedetails`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `employeedetails` (
  `name` tinyint NOT NULL,
  `position` tinyint NOT NULL,
  `manager` tinyint NOT NULL,
  `sales` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employees` (
  `employee_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `position` varchar(255) NOT NULL,
  `contact` varchar(255) DEFAULT NULL,
  `manager` int(11) DEFAULT NULL,
  PRIMARY KEY (`employee_id`),
  UNIQUE KEY `employee_id` (`employee_id`),
  KEY `contact` (`contact`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`contact`) REFERENCES `contacts` (`address`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'Drew Rodman','Manager','34B Mary St',NULL),(5,'vx xrgdstrgdrt','Specialist',NULL,1),(6,'cs fxcrsgfrsf','Specialist',NULL,1),(7,'fsvfrsfdrsf','Specialist',NULL,1),(8,'Jonathan','Genius',NULL,1),(9,'','Specialist',NULL,1);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 trigger employee_quit
before delete on employees 
for each row begin
	delete from employee_shifts 
	where employee = OLD.employee_id;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary table structure for view `employeesales`
--

DROP TABLE IF EXISTS `employeesales`;
/*!50001 DROP VIEW IF EXISTS `employeesales`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `employeesales` (
  `name` tinyint NOT NULL,
  `sales` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `onholdproducts`
--

DROP TABLE IF EXISTS `onholdproducts`;
/*!50001 DROP VIEW IF EXISTS `onholdproducts`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `onholdproducts` (
  `model` tinyint NOT NULL,
  `serial_number` tinyint NOT NULL,
  `price` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `manufacturer` tinyint NOT NULL,
  `bucket` tinyint NOT NULL,
  `store` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `model` varchar(10) NOT NULL DEFAULT '',
  `serial_number` varchar(12) NOT NULL DEFAULT '',
  `name` varchar(255) NOT NULL,
  `manufacturer` varchar(255) NOT NULL,
  `price` decimal(10,0) NOT NULL,
  `bucket` varchar(15) NOT NULL,
  `store` int(11) NOT NULL,
  PRIMARY KEY (`model`,`serial_number`),
  KEY `products_ibfk_1` (`store`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`store`) REFERENCES `stores` (`store_number`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES ('MD245LL/A','C02LGF54ZG2','Macbook Pro','Apple',1999,'sellable',318),('MD528LL/A','F24LNBLS523','iPad Mini','Apple',329,'sellable',318);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receipts`
--

DROP TABLE IF EXISTS `receipts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `receipts` (
  `receipt_id` int(11) NOT NULL AUTO_INCREMENT,
  `total` decimal(10,0) NOT NULL,
  `date` datetime NOT NULL,
  `customer` int(11) DEFAULT NULL,
  `product` varchar(255) DEFAULT NULL,
  `cashier` int(11) DEFAULT NULL,
  `store` int(11) DEFAULT NULL,
  UNIQUE KEY `receipt_id` (`receipt_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receipts`
--

LOCK TABLES `receipts` WRITE;
/*!40000 ALTER TABLE `receipts` DISABLE KEYS */;
INSERT INTO `receipts` VALUES (1,200,'2013-11-29 11:41:59',1,'C02LGF54ZG2',1,1),(2,200,'2013-11-29 11:42:23',1,'C02LGF54ZG2',1,1),(3,200,'2013-11-29 11:45:08',1,'C02LGF54ZG2',1,1),(5,200,'2013-11-29 11:48:15',1,NULL,1,1),(7,200,'2013-11-29 11:51:04',1,NULL,7,1);
/*!40000 ALTER TABLE `receipts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `rtwproducts`
--

DROP TABLE IF EXISTS `rtwproducts`;
/*!50001 DROP VIEW IF EXISTS `rtwproducts`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `rtwproducts` (
  `model` tinyint NOT NULL,
  `serial_number` tinyint NOT NULL,
  `price` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `manufacturer` tinyint NOT NULL,
  `bucket` tinyint NOT NULL,
  `store` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `sellableproducts`
--

DROP TABLE IF EXISTS `sellableproducts`;
/*!50001 DROP VIEW IF EXISTS `sellableproducts`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `sellableproducts` (
  `model` tinyint NOT NULL,
  `serial_number` tinyint NOT NULL,
  `price` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `manufacturer` tinyint NOT NULL,
  `bucket` tinyint NOT NULL,
  `store` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `serviced_products`
--

DROP TABLE IF EXISTS `serviced_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `serviced_products` (
  `repair_number` int(11) NOT NULL AUTO_INCREMENT,
  `issue` varchar(255) DEFAULT NULL,
  `store` int(11) DEFAULT NULL,
  `customer` int(11) DEFAULT NULL,
  `technician` int(11) DEFAULT NULL,
  `product` int(11) DEFAULT NULL,
  PRIMARY KEY (`repair_number`),
  UNIQUE KEY `repair_number` (`repair_number`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `serviced_products`
--

LOCK TABLES `serviced_products` WRITE;
/*!40000 ALTER TABLE `serviced_products` DISABLE KEYS */;
/*!40000 ALTER TABLE `serviced_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `soldproducts`
--

DROP TABLE IF EXISTS `soldproducts`;
/*!50001 DROP VIEW IF EXISTS `soldproducts`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `soldproducts` (
  `model` tinyint NOT NULL,
  `serial_number` tinyint NOT NULL,
  `price` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `manufacturer` tinyint NOT NULL,
  `bucket` tinyint NOT NULL,
  `store` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `stores`
--

DROP TABLE IF EXISTS `stores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stores` (
  `store_number` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `lead_manager` int(11) DEFAULT NULL,
  UNIQUE KEY `store_number` (`store_number`),
  KEY `lead_manager` (`lead_manager`),
  CONSTRAINT `stores_ibfk_1` FOREIGN KEY (`lead_manager`) REFERENCES `employees` (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=319 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stores`
--

LOCK TABLES `stores` WRITE;
/*!40000 ALTER TABLE `stores` DISABLE KEYS */;
INSERT INTO `stores` VALUES (318,'Apple Store',1);
/*!40000 ALTER TABLE `stores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `contact_info`
--

/*!50001 DROP TABLE IF EXISTS `contact_info`*/;
/*!50001 DROP VIEW IF EXISTS `contact_info`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `contact_info` AS select `contacts`.`phone` AS `phone`,`contacts`.`email` AS `email` from (`contacts` join `employees`) where (`contacts`.`address` = (select `contacts`.`address` from `employees` where (`employees`.`employee_id` = `employees`.`employee_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `employeedetails`
--

/*!50001 DROP TABLE IF EXISTS `employeedetails`*/;
/*!50001 DROP VIEW IF EXISTS `employeedetails`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `employeedetails` AS select `e1`.`name` AS `name`,`e1`.`position` AS `position`,`e2`.`name` AS `manager`,`employeesales`.`sales` AS `sales` from ((`employees` `e1` join `employees` `e2`) join `employeesales` on((`e1`.`manager` = `e2`.`employee_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `employeesales`
--

/*!50001 DROP TABLE IF EXISTS `employeesales`*/;
/*!50001 DROP VIEW IF EXISTS `employeesales`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `employeesales` AS select `employees`.`name` AS `name`,sum(`receipts`.`total`) AS `sales` from (`receipts` join `employees`) where (`receipts`.`cashier` = `employees`.`employee_id`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `onholdproducts`
--

/*!50001 DROP TABLE IF EXISTS `onholdproducts`*/;
/*!50001 DROP VIEW IF EXISTS `onholdproducts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `onholdproducts` AS select `products`.`model` AS `model`,`products`.`serial_number` AS `serial_number`,`products`.`price` AS `price`,`products`.`name` AS `name`,`products`.`manufacturer` AS `manufacturer`,`products`.`bucket` AS `bucket`,`products`.`store` AS `store` from `products` where (`products`.`bucket` = 'on_hold') */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `rtwproducts`
--

/*!50001 DROP TABLE IF EXISTS `rtwproducts`*/;
/*!50001 DROP VIEW IF EXISTS `rtwproducts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `rtwproducts` AS select `products`.`model` AS `model`,`products`.`serial_number` AS `serial_number`,`products`.`price` AS `price`,`products`.`name` AS `name`,`products`.`manufacturer` AS `manufacturer`,`products`.`bucket` AS `bucket`,`products`.`store` AS `store` from `products` where (`products`.`bucket` = 'rtw') */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `sellableproducts`
--

/*!50001 DROP TABLE IF EXISTS `sellableproducts`*/;
/*!50001 DROP VIEW IF EXISTS `sellableproducts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `sellableproducts` AS select `products`.`model` AS `model`,`products`.`serial_number` AS `serial_number`,`products`.`price` AS `price`,`products`.`name` AS `name`,`products`.`manufacturer` AS `manufacturer`,`products`.`bucket` AS `bucket`,`products`.`store` AS `store` from `products` where (`products`.`bucket` = 'sellable') */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `soldproducts`
--

/*!50001 DROP TABLE IF EXISTS `soldproducts`*/;
/*!50001 DROP VIEW IF EXISTS `soldproducts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `soldproducts` AS select `products`.`model` AS `model`,`products`.`serial_number` AS `serial_number`,`products`.`price` AS `price`,`products`.`name` AS `name`,`products`.`manufacturer` AS `manufacturer`,`products`.`bucket` AS `bucket`,`products`.`store` AS `store` from `products` where (`products`.`bucket` = 'sold') */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-11-29 11:52:41
