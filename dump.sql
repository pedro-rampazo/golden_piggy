-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: golden_piggy
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.22.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `competition`
--

DROP TABLE IF EXISTS `competition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `competition` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `competition`
--

LOCK TABLES `competition` WRITE;
/*!40000 ALTER TABLE `competition` DISABLE KEYS */;
/*!40000 ALTER TABLE `competition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hunch`
--

DROP TABLE IF EXISTS `hunch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hunch` (
  `id` int NOT NULL AUTO_INCREMENT,
  `home_score` int NOT NULL,
  `away_score` int NOT NULL,
  `hunch_score` int DEFAULT NULL,
  `id_match` int NOT NULL,
  `id_player` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_match` (`id_match`),
  KEY `id_player` (`id_player`),
  CONSTRAINT `hunch_ibfk_1` FOREIGN KEY (`id_match`) REFERENCES `match` (`id`),
  CONSTRAINT `hunch_ibfk_2` FOREIGN KEY (`id_player`) REFERENCES `player` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hunch`
--

LOCK TABLES `hunch` WRITE;
/*!40000 ALTER TABLE `hunch` DISABLE KEYS */;
/*!40000 ALTER TABLE `hunch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `match`
--

DROP TABLE IF EXISTS `match`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `match` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `home_score` int DEFAULT NULL,
  `away_score` int DEFAULT NULL,
  `local` varchar(100) DEFAULT NULL,
  `id_competition` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_competition` (`id_competition`),
  CONSTRAINT `match_ibfk_1` FOREIGN KEY (`id_competition`) REFERENCES `competition` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match`
--

LOCK TABLES `match` WRITE;
/*!40000 ALTER TABLE `match` DISABLE KEYS */;
/*!40000 ALTER TABLE `match` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `match_team`
--

DROP TABLE IF EXISTS `match_team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `match_team` (
  `id` int NOT NULL AUTO_INCREMENT,
  `home_team` varchar(100) NOT NULL,
  `away_team` varchar(100) NOT NULL,
  `id_match` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_match` (`id_match`),
  CONSTRAINT `match_team_ibfk_1` FOREIGN KEY (`id_match`) REFERENCES `match` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match_team`
--

LOCK TABLES `match_team` WRITE;
/*!40000 ALTER TABLE `match_team` DISABLE KEYS */;
/*!40000 ALTER TABLE `match_team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player`
--

DROP TABLE IF EXISTS `player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `player_score` int DEFAULT NULL,
  `accurate_hunch` int DEFAULT NULL,
  `hunch_quantity` int DEFAULT NULL,
  `zero_points` int DEFAULT NULL,
  `id_competition` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_competition` (`id_competition`),
  CONSTRAINT `player_ibfk_1` FOREIGN KEY (`id_competition`) REFERENCES `competition` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player`
--

LOCK TABLES `player` WRITE;
/*!40000 ALTER TABLE `player` DISABLE KEYS */;
/*!40000 ALTER TABLE `player` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team`
--

DROP TABLE IF EXISTS `team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `team` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `emblem` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team`
--

LOCK TABLES `team` WRITE;
/*!40000 ALTER TABLE `team` DISABLE KEYS */;
INSERT INTO `team` VALUES (1,'Palmeiras','emblems/palmeiras.png'),(2,'Água Santa','emblems/agua_santa.png'),(3,'América-MG','emblems/america_mg.png'),(4,'Athletico-PR','emblems/athletico_pr.png'),(5,'Atlético-MG','emblems/atletico_mg.png'),(6,'Bahia','emblems/bahia.png'),(7,'Botafogo','emblems/botafogo.png'),(8,'Botafogo-SP','emblems/botafogo_sp.png'),(9,'Corinthians','emblems/corinthians.png'),(10,'Coritiba','emblems/coritiba.png'),(11,'Cruzeiro','emblems/cruzeiro.png'),(12,'Cuiabá','emblems/cuiaba.png'),(13,'Ferroviária','emblems/ferroviaria.png'),(14,'Flamengo','emblems/flamengo.png'),(15,'Fluminense','emblems/fluminense.png'),(16,'Fortaleza','emblems/fortaleza.png'),(17,'Goiás','emblems/goias.png'),(18,'Grêmio','emblems/gremio.png'),(19,'Guarani','emblems/guarani.png'),(20,'Inter De Limeira','emblems/inter_de_limeira.png'),(21,'Internacional','emblems/internacional.png'),(22,'Ituano','emblems/ituano.png'),(23,'Mirassol','emblems/mirassol.png'),(24,'Portuguesa','emblems/portuguesa.png'),(25,'Red Bull Bragantino','emblems/red_bull_bragantino.png'),(26,'Santo André','emblems/santo_andre.png'),(27,'Santos','emblems/santos.png'),(28,'São Bento','emblems/sao_bento.png'),(29,'São Bernardo','emblems/sao_bernardo.png'),(30,'São Paulo','emblems/sao_paulo.png'),(31,'Vasco','emblems/vasco.png');
/*!40000 ALTER TABLE `team` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-09 17:08:06
