CREATE DATABASE  IF NOT EXISTS `avito_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `avito_db`;
-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: avito_db
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ads`
--

DROP TABLE IF EXISTS `ads`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ads` (
  `idAds` int(11) NOT NULL AUTO_INCREMENT,
  `price` int(11) NOT NULL,
  `addressFull` varchar(45) DEFAULT NULL,
  `primary` tinyint(4) NOT NULL,
  `date` datetime NOT NULL,
  `linkAd` varchar(200) NOT NULL,
  `views` int(11) NOT NULL,
  `idAdInSite` varchar(45) NOT NULL,
  `seller` varchar(100) NOT NULL,
  `linkSeller` varchar(200) NOT NULL,
  `floor` int(11) DEFAULT NULL,
  `numberOfFloors` int(11) NOT NULL,
  `numberOfRooms` int(11) DEFAULT NULL,
  `livingSpace` int(11) DEFAULT NULL,
  `totalArea` int(11) NOT NULL,
  `kithenArea` int(11) DEFAULT NULL,
  `yearOfConstruction` int(11) DEFAULT NULL,
  `finishing` varchar(45) DEFAULT NULL,
  `developer` varchar(150) DEFAULT NULL,
  `nameOfTheNewBulding` varchar(150) DEFAULT NULL,
  `thePlots` int(11) DEFAULT NULL,
  `distanseToCity` int(11) DEFAULT NULL,
  `online` tinyint(4) NOT NULL,
  `ownership` varchar(45) NOT NULL,
  `idKindOfProperty` int(11) NOT NULL,
  `species_idSpecie` int(11) NOT NULL,
  `lacality_idlacality` int(11) NOT NULL,
  `idMaterial` int(11) NOT NULL,
  PRIMARY KEY (`idAds`),
  UNIQUE KEY `linkAd_UNIQUE` (`linkAd`),
  UNIQUE KEY `idAdInSite_UNIQUE` (`idAdInSite`),
  KEY `fk_ads_kindOfPropertys1_idx` (`idKindOfProperty`),
  KEY `fk_ads_species1_idx` (`species_idSpecie`),
  KEY `fk_ads_lacality1_idx` (`lacality_idlacality`),
  KEY `fk_ads_buildingmaterials_idx` (`idMaterial`),
  CONSTRAINT `fk_ads_buildingmaterials` FOREIGN KEY (`idMaterial`) REFERENCES `buildingmaterials` (`idMaterial`) ON UPDATE CASCADE,
  CONSTRAINT `fk_ads_kindOfPropertys1` FOREIGN KEY (`idKindOfProperty`) REFERENCES `kindofpropertys` (`idKindOfProperty`),
  CONSTRAINT `fk_ads_lacality1` FOREIGN KEY (`lacality_idlacality`) REFERENCES `lacality` (`idlacality`),
  CONSTRAINT `fk_ads_species1` FOREIGN KEY (`species_idSpecie`) REFERENCES `species` (`idSpecie`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ads`
--

LOCK TABLES `ads` WRITE;
/*!40000 ALTER TABLE `ads` DISABLE KEYS */;
/*!40000 ALTER TABLE `ads` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-03  5:06:46
