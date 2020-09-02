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
-- Table structure for table `lacality`
--

DROP TABLE IF EXISTS `lacality`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lacality` (
  `idlacality` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `idDistrict` int(11) NOT NULL,
  `idRegion` int(11) NOT NULL,
  `population` int(11) DEFAULT NULL,
  PRIMARY KEY (`idlacality`),
  KEY `fk_lacality_district_idx` (`idDistrict`),
  KEY `fk_lacality_regions1_idx` (`idRegion`),
  CONSTRAINT `fk_lacality_district` FOREIGN KEY (`idDistrict`) REFERENCES `district` (`idDistrict`),
  CONSTRAINT `fk_lacality_regions1` FOREIGN KEY (`idRegion`) REFERENCES `regions` (`idRegions`)
) ENGINE=InnoDB AUTO_INCREMENT=626 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lacality`
--

LOCK TABLES `lacality` WRITE;
/*!40000 ALTER TABLE `lacality` DISABLE KEYS */;
INSERT INTO `lacality` VALUES (1,'г. Благовещенск',1,1,226385),(2,'село Белогорье',1,1,2736),(3,'железнодорожная станция Белогорье',1,1,26),(4,'посёлок Мухинка',1,1,124),(5,'посёлок Плодопитомник',1,1,1070),(6,'железнодорожная станция Призейская',1,1,210),(7,'село Садовое',1,1,1077),(8,'г. Белогорск',2,1,65315),(9,'село Низинное',2,1,461),(10,'г. Зея',3,1,22984),(11,'г. Райчихинск',4,1,16784),(12,'село Угольное',4,1,36),(13,'поселок Широкий',4,1,1226),(14,'поселок Зельвино',4,1,1408),(15,'г. Свободный',5,1,54017),(16,'г. Тында',6,1,33177),(17,'г. Шимановск',7,1,18566),(18,'пгт Новорайчихинск',8,1,1842),(19,'пгт Прогресс',8,1,9517),(20,'посёлок Кивдинский',8,1,14),(21,'г. Циолковский',9,1,7188),(22,'пгт  Архара',10,1,8508),(23,'село Бон',10,1,7),(24,'железнодорожная станция Журавли',10,1,3),(25,'село Антоновка',10,1,84),(26,'село Красная Горка',10,1,4),(27,'село Аркадьевка',10,1,602),(28,'село Черноберезовка',10,1,60),(29,'село Вольное',10,1,76),(30,'село Орловка',10,1,37),(31,'село Грибовка',10,1,177),(32,'село Ерахта',10,1,5),(33,'село Могилевка',10,1,60),(34,'село Иннокентьевка',10,1,383),(35,'село Красный Луч',10,1,24),(36,'село Касаткино',10,1,234),(37,'село Журавлевка',10,1,156),(38,'село Новопокровка',10,1,87),(39,'село Сагибово',10,1,62),(40,'село Кундур',10,1,654),(41,'село Казачий',10,1,2),(42,'село Тарманчукан',10,1,4),(43,'село Ленинское',10,1,276),(44,'село Красный Исток',10,1,46),(45,'село Михайловка',10,1,10),(46,'село Новосергеевка',10,1,77),(47,'железнодорожная станция Богучан',10,1,56),(48,'село Новоспасск',10,1,182),(49,'село Домикан',10,1,168),(50,'село Казановка',10,1,33),(51,'село Свободное',10,1,2),(52,'село Отважное',10,1,640),(53,'село Заречное',10,1,41),(54,'село Каменный Карьер',10,1,95),(55,'железнодорожная станция Татакан',10,1,85),(56,'село Северное',10,1,162),(57,'село Скобельцыно',10,1,32),(58,'село Украинка',10,1,17),(59,'село Урил',10,1,77),(60,'железнодорожная станция Рачи',10,1,1),(61,'село Черниговка',10,1,130),(62,'село Гуликовка',10,1,12),(63,'железнодорожная станция Домикан',10,1,57),(64,'село Каменка',10,1,26),(65,'железнодорожная станция Кулустай',10,1,4),(66,'село Левый Берег',10,1,1),(67,'село Новодомикан',10,1,54),(68,'село Петропавловка',10,1,1),(69,'село Ядрино',10,1,458),(70,'железнодорожная станция Есауловка',10,1,2),(71,'село Белоцерковка',2,1,226),(72,'село Васильевка',2,1,2145),(73,'село Круглое',2,1,68),(74,'село Междугранка',2,1,355),(75,'село Павловка',2,1,205),(76,'село Великокнязевка',2,1,721),(77,'село Комиссаровка',2,1,91),(78,'село Новоандреевка',2,1,116),(79,'село Возжаевка',2,1,4963),(80,'село Амурское',2,1,924),(81,'село Дубровка',2,1,56),(82,'село Кустанаевка',2,1,381),(83,'село Камышевка',2,1,51),(84,'село Лозовое',2,1,0),(85,'село Лукьяновка',2,1,136),(86,'село Лохвицы',2,1,552),(87,'село Савельевка',2,1,95),(88,'село Некрасовка',2,1,403),(89,'село Захарьевка',2,1,15),(90,'село Новоназаровка',2,1,49),(91,'село Новоселитьба',2,1,39),(92,'село Никольское',2,1,1402),(93,'село Киселеозерка',2,1,204),(94,'село Ключи',2,1,179),(95,'село Новое',2,1,409),(96,'село Луговое',2,1,39),(97,'село Мостовое',2,1,11),(98,'село Заречное',2,1,382),(99,'село Озеряне',2,1,98),(100,'село Чернетчено',2,1,39),(101,'село Пригородное',2,1,408),(102,'село Мирное',2,1,222),(103,'село Светиловка',2,1,400),(104,'село Томичи',2,1,1391),(105,'село Поляное',2,1,101),(106,'село Успеновка',2,1,303),(107,'село Волково',1,1,2112),(108,'село Ровное',1,1,429),(109,'село Грибское',1,1,999),(110,'село Дроново',1,1,252),(111,'село Передовое',1,1,167),(112,'село Удобное',1,1,117),(113,'село Гродеково',1,1,513),(114,'посёлок Заречный',1,1,160),(115,'село Каникурган',1,1,224),(116,'село Марково',1,1,1336),(117,'село Михайловка',1,1,544),(118,'село Грязнушка',1,1,323),(119,'село Натальино',1,1,303),(120,'село Новопетровка',1,1,724),(121,'село Егорьевка',1,1,174),(122,'село Новинка',1,1,144),(123,'село Прядчино',1,1,279),(124,'село Новотроицкое',1,1,899),(125,'село Кантон-Коммуна',1,1,163),(126,'село Сергеевка',1,1,1141),(127,'село Бибиково',1,1,169),(128,'село Усть-Ивановка',1,1,2664),(129,'село Владимировка',1,1,1096),(130,'село Чигири',1,1,11889),(131,'посёлок Вадимово',1,1,3),(132,'село Верхнеблаговещенское',1,1,747),(133,'село Игнатьево',1,1,1036),(134,'пгт Бурея',11,1,4021),(135,'село Кивдо-Тюкан',11,1,38),(136,'село Муравка',11,1,70),(137,'железнодорожная станция Тюкан',11,1,5),(138,'пгт Новобурейский',11,1,6688),(139,'село Николаевка',11,1,747),(140,'пгт Талакан',11,1,4139),(141,'село Алексеевка',11,1,194),(142,'село Асташиха',11,1,95),(143,'село Виноградовка',11,1,400),(144,'село Долдыкан',11,1,363),(145,'село Малиновка',11,1,1056),(146,'село Гомелевка',11,1,0),(147,'село Усть-Кивда',11,1,144),(148,'село Безозерное',11,1,383),(149,'село Безымянное',11,1,98),(150,'село Родионовка',11,1,242),(151,'село Семеновка',11,1,90),(152,'село Трехречье',11,1,30),(153,'село Старая Райчиха',11,1,317),(154,'село Успеновка',11,1,256),(155,'село Правая Райчиха',11,1,17),(156,'г. Завитинск',12,1,10215),(157,'село Новоалексеевка',12,1,104),(158,'железнодорожная станция Тур',12,1,0),(159,'село Червоная Армия',12,1,180),(160,'село Албазинка',12,1,168),(161,'село Платово',12,1,28),(162,'село Антоновка',12,1,425),(163,'село Ленино',12,1,35),(164,'село Белый Яр',12,1,144),(165,'село Аврамовка',12,1,30),(166,'село Болдыревка',12,1,450),(167,'село Верхнеильиновка',12,1,133),(168,'село Житомировка',12,1,0),(169,'село Иннокентьевка',12,1,227),(170,'село Демьяновка',12,1,95),(171,'железнодорожная станция Демьяновка',12,1,0),(172,'село Ивановка',12,1,137),(173,'село Куприяновка',12,1,315),(174,'село Подоловка',12,1,161),(175,'село Федоровка',12,1,23),(176,'село Преображеновка',12,1,165),(177,'село Валуево',12,1,104),(178,'железнодорожная станция Дея',12,1,17),(179,'село Успеновка',12,1,252),(180,'село Камышенка',12,1,192),(181,'село Алгач',3,1,400),(182,'село Амуро-Балтийск',3,1,181),(183,'село Сиан',3,1,50),(184,'посёлок Береговой',3,1,1295),(185,'посёлок Кировский',3,1,18),(186,'село Бомнак',3,1,419),(187,'посёлок Верхнезейск',3,1,1277),(188,'посёлок Горный',3,1,733),(189,'поселок Дугда',3,1,670),(190,'село Ивановка',3,1,306),(191,'село Николаевка-2',3,1,13),(192,'село Александровка',3,1,158),(193,'село Алексеевка',3,1,0),(194,'село Березовка',3,1,48),(195,'село Николаевка',3,1,251),(196,'село Овсянка',3,1,2782),(197,'посёлок Огорон',3,1,258),(198,'село Октябрьский',3,1,957),(199,'посёлок Ясный',3,1,8),(200,'посёлок Поляковский',3,1,236),(201,'посёлок Снежногорский',3,1,338),(202,'село Сосновый Бор',3,1,738),(203,'село Гулик',3,1,264),(204,'село Заречная Слобода',3,1,588),(205,'село Золотая Гора',3,1,55),(206,'посёлок Тунгала',3,1,511),(207,'село Умлекан',3,1,234),(208,'село Рублевка',3,1,68),(209,'посёлок Хвойный',3,1,200),(210,'село Чалбачи',3,1,242),(211,'посёлок Юбилейный',3,1,379),(212,'село Анновка',13,1,558),(213,'село Большеозерка',13,1,242),(214,'село Вишневка',13,1,14),(215,'село Березовка',13,1,3093),(216,'село Петропавловка',13,1,705),(217,'село Семиозерка',13,1,557),(218,'село Дмитриевка',13,1,971),(219,'село Ерковцы',13,1,915),(220,'село Черкасовка',13,1,21),(221,'село Ивановка',13,1,6487),(222,'село Вознесеновка',13,1,4),(223,'село Крещеновка',13,1,168),(224,'село Луговое',13,1,262),(225,'село Успеновка',13,1,356),(226,'село Константиноградовка',13,1,496),(227,'село Николаевка',13,1,266),(228,'село Новопокровка',13,1,160),(229,'село Новоалексеевка',13,1,586),(230,'село Ракитное',13,1,59),(231,'село Среднебелое',13,1,707),(232,'село Полевое',13,1,73),(233,'село Правовосточное',13,1,308),(234,'село Некрасовка',13,1,82),(235,'село Садовое',13,1,78),(236,'село Андреевка',13,1,224),(237,'село Богословка',13,1,34),(238,'село Солнечное',13,1,407),(239,'село Надежденское',13,1,76),(240,'село Среднебелая',13,1,3764),(241,'село Приозерное',13,1,180),(242,'село Троицкое',13,1,400),(243,'село Черемхово',13,1,811),(244,'село Богородское',13,1,539),(245,'село Верхняя Полтавка',14,1,617),(246,'село Средняя Полтавка',14,1,246),(247,'село Верхний Уртуй',14,1,406),(248,'село Зеньковка',14,1,434),(249,'село Золотоножка',14,1,205),(250,'село Ключи',14,1,762),(251,'село Коврижка',14,1,370),(252,'село Октябрьское',14,1,102),(253,'село Константиновка',14,1,5197),(254,'село Крестовоздвиженка',14,1,957),(255,'село Нижняя Полтавка',14,1,1143),(256,'село Новопетровка',14,1,510),(257,'село Войково',14,1,190),(258,'село Орловка',14,1,269),(259,'село Новотроицкое',14,1,446),(260,'село Семидомка',14,1,318),(261,'пгт Магдагачи',15,1,9895),(262,'железнодорожный блок-пост Красная Падь',15,1,11),(263,'пгт Сиваки',15,1,1568),(264,'посёлок 16 Км',15,1,0),(265,'пгт Ушумун',15,1,1899),(266,'село Гонжа',15,1,705),(267,'село Кислый Ключ',15,1,24),(268,'железнодорожная станция Нюкжа',15,1,0),(269,'посёлок Гудачи',15,1,368),(270,'посёлок Дактуй',15,1,536),(271,'посёлок Апрельский',15,1,41),(272,'село Пионер',15,1,30),(273,'железнодорожная станция Сулус',15,1,28),(274,'железнодорожная станция Тымерсоль',15,1,4),(275,'село Кузнецово',15,1,178),(276,'село Толбузино',15,1,178),(277,'село Тыгда',15,1,2948),(278,'село Новопокровка',15,1,0),(279,'посёлок Чалганы',15,1,388),(280,'село Черняево',15,1,791),(281,'село Калиновка',15,1,0),(282,'село Белоярово',16,1,901),(283,'село Каменка',16,1,10),(284,'село Юбилейное',16,1,85),(285,'село Богословка',16,1,213),(286,'село Козловка',16,1,67),(287,'село Дмитриевка',16,1,162),(288,'село Бичура',16,1,125),(289,'село Каничи',16,1,53),(290,'село Паутовка',16,1,90),(291,'село Маргаритовка',16,1,323),(292,'село Красноярово',16,1,959),(293,'село Антоновка',16,1,36),(294,'село Леонтьевка',16,1,68),(295,'село Михайловка',16,1,105),(296,'село Петровка',16,1,111),(297,'село Мазаново',16,1,636),(298,'посёлок Ивановский',16,1,393),(299,'посёлок Майский',16,1,83),(300,'село Молчаново',16,1,445),(301,'село Поповка',16,1,410),(302,'село Спицыно',16,1,0),(303,'село Новокиевский Увал',16,1,3762),(304,'село Новокиевка',16,1,685),(305,'посёлок Пионерский',16,1,275),(306,'село Раздольное',16,1,125),(307,'село Дружное',16,1,15),(308,'село Романкауцы',16,1,135),(309,'село Новороссийка',16,1,263),(310,'село Слава',16,1,1),(311,'село Практичи',16,1,363),(312,'село Сохатино',16,1,71),(313,'село Путятино',16,1,234),(314,'село Таскино',16,1,265),(315,'село Сапроново',16,1,534),(316,'село Алексеевка',16,1,37),(317,'село Кольцовка',16,1,37),(318,'село Христиновка',16,1,36),(319,'село Угловое',16,1,493),(320,'село Абайкан',16,1,4),(321,'село Ульма',16,1,107),(322,'село Воскресеновка',17,1,213),(323,'железнодорожная станция Воскресеновка',17,1,95),(324,'село Кавказ',17,1,60),(325,'село Шумиловка',17,1,49),(326,'село Дим',17,1,661),(327,'село Дубовое',17,1,290),(328,'село Привольное',17,1,45),(329,'село Шурино',17,1,64),(330,'село Зеленый Бор',17,1,489),(331,'село Красный Яр',17,1,112),(332,'село Черемисино',17,1,122),(333,'село Нижняя Ильиновка',17,1,274),(334,'село Ярославка',17,1,65),(335,'село Калинино',17,1,536),(336,'село Винниково',17,1,162),(337,'село Коршуновка',17,1,402),(338,'село Красный Восток',17,1,75),(339,'село Нижнезавитинка',17,1,51),(340,'село Михайловка',17,1,691),(341,'село Арсентьевка',17,1,166),(342,'село Новогеоргиевка',17,1,15),(343,'село Петропавловка',17,1,214),(344,'село Новочесноково',17,1,537),(345,'село Высокое',17,1,2),(346,'село Куприяново',17,1,131),(347,'село Поярково',17,1,6590),(348,'село Чесноково',17,1,672),(349,'село Красная Орловка',17,1,125),(350,'село Шадрино',17,1,196),(351,'село Борисоглебка',18,1,175),(352,'село Ильиновка',18,1,180),(353,'село Варваровка',18,1,2460),(354,'посёлок Восточный',18,1,1240),(355,'посёлок Прибрежный',18,1,75),(356,'село Екатеринославка',18,1,9836),(357,'село Зорино',18,1,0),(358,'посёлок Нагорный',18,1,33),(359,'село Короли',18,1,205),(360,'село Георгиевка',18,1,32),(361,'село Смирновка',18,1,9),(362,'село Смелое',18,1,122),(363,'село Беляковка',18,1,10),(364,'село Ясная Поляна',18,1,2),(365,'село Максимовка',18,1,312),(366,'село Кутилово',18,1,45),(367,'посёлок Мухинский',18,1,543),(368,'село Черемушки',18,1,104),(369,'село Николо-Александровка',18,1,479),(370,'село Покровка',18,1,139),(371,'село Новомихайловка',18,1,388),(372,'село Сергее-Федоровка',18,1,115),(373,'железнодорожная станция Троебратка',18,1,22),(374,'село Харьковка',18,1,3),(375,'село Панино',18,1,184),(376,'посёлок Южный',18,1,74),(377,'село Переясловка',18,1,52),(378,'село Преображеновка',18,1,102),(379,'село Песчаноозерка',18,1,436),(380,'село Романовка',18,1,411),(381,'село Борисово',18,1,0),(382,'село Марьяновка',18,1,153),(383,'посёлок Трудовой',18,1,97),(384,'посёлок Заозерный',18,1,58),(385,'посёлок Увальный',18,1,66),(386,'село Амаранка',19,1,214),(387,'село Восточная Нива',19,1,5),(388,'село Новониколаевка',19,1,109),(389,'село Дальневосточное',19,1,241),(390,'село Григорьевка',19,1,66),(391,'село Урожайное',19,1,7),(392,'село Знаменка',19,1,399),(393,'село Кузьмичи',19,1,32),(394,'село Каховка',19,1,305),(395,'село Новый Быт',19,1,140),(396,'село Серединное',19,1,18),(397,'село Поздеевка',19,1,1456),(398,'село Верхнебелое',19,1,251),(399,'село Новороссийка',19,1,140),(400,'село Рогозовка',19,1,262),(401,'село Вознесеновка',19,1,85),(402,'село Высокое',19,1,12),(403,'село Климовка',19,1,17),(404,'село Ромны',19,1,2732),(405,'село Калиновка',19,1,185),(406,'село Святоруссовка',19,1,291),(407,'село Любимое',19,1,108),(408,'село Морозовка',19,1,65),(409,'село Чергали',19,1,262),(410,'село Братолюбовка',19,1,93),(411,'село Придорожное',19,1,35),(412,'село Райгородка',19,1,26),(413,'село Смоляное',19,1,121),(414,'село Хохлатское',19,1,33),(415,'село Дмитриевка',5,1,396),(416,'посёлок Юхта',5,1,417),(417,'посёлок Юхта-3',5,1,85),(418,'село Усть-Пера',5,1,343),(419,'село Желтоярово',5,1,470),(420,'село Гащенка',5,1,141),(421,'село Заган',5,1,94),(422,'село Новоникольск',5,1,64),(423,'село Черниговка',5,1,451),(424,'село Загорная Селитьба',5,1,420),(425,'село Климоуцы',5,1,724),(426,'село Новостепановка',5,1,200),(427,'село Талали',5,1,236),(428,'село Костюковка',5,1,419),(429,'село Зиговка',5,1,124),(430,'село Малый Эргель',5,1,24),(431,'село Серебрянка',5,1,236),(432,'село Глухари',5,1,159),(433,'село Курган',5,1,48),(434,'село Голубое',5,1,171),(435,'село Малая Сазанка',5,1,1856),(436,'село Москвитино',5,1,421),(437,'посёлок Источный',5,1,61),(438,'село Нижние Бузули',5,1,967),(439,'село Новоострополь',5,1,56),(440,'село Новгородка',5,1,807),(441,'село Бардагон',5,1,170),(442,'посёлок Подгорный',5,1,265),(443,'село Новоивановка',5,1,486),(444,'село Рогачевка',5,1,311),(445,'село Буссе',5,1,480),(446,'село Петропавловка',5,1,84),(447,'село Семеновка',5,1,317),(448,'село Сукромли',5,1,123),(449,'село Маркучи',5,1,183),(450,'село Сычевка',5,1,565),(451,'село Гуран',5,1,141),(452,'село Черновка',5,1,621),(453,'село Бузули',5,1,184),(454,'село Разливная',5,1,160),(455,'село Чембары',5,1,375),(456,'пгт Экимчан',20,1,986),(457,'пгт Токур',20,1,816),(458,'пгт Февральск',20,1,4560),(459,'село Февральское',20,1,315),(460,'поселок Златоустовск',20,1,639),(461,'посёлок Ольгинск',20,1,100),(462,'село Ивановское',20,1,351),(463,'посёлок Иса',20,1,411),(464,'село Коболдо',20,1,359),(465,'село Огоджа',20,1,304),(466,'село Норск',20,1,279),(467,'село Бысса',20,1,41),(468,'село Стойба',20,1,620),(469,'село Селемджинск',20,1,21),(470,'пгт Серышево',21,1,9438),(471,'железнодорожная станция Арга',21,1,555),(472,'село Введеновка',21,1,255),(473,'село Веселое',21,1,84),(474,'село Большая Сазанка',21,1,585),(475,'село Воронжа',21,1,46),(476,'село Ключики',21,1,161),(477,'село Водораздельное',21,1,205),(478,'село Милехино',21,1,54),(479,'село Казанка',21,1,421),(480,'село Калиновка',21,1,0),(481,'село Липовка',21,1,58),(482,'село Сретенка',21,1,40),(483,'село Лебяжье',21,1,343),(484,'село Белоусовка',21,1,42),(485,'село Лермонтово',21,1,240),(486,'село Бирма',21,1,43),(487,'село Ближний Сахалин',21,1,37),(488,'село Павловка',21,1,49),(489,'село Лиманное',21,1,227),(490,'село Пушкино',21,1,0),(491,'село Новосергеевка',21,1,432),(492,'село Паруновка',21,1,302),(493,'село Рождественка',21,1,266),(494,'село Озерное',21,1,523),(495,'село Белоногово',21,1,1475),(496,'село Добрянка',21,1,181),(497,'село Поляна',21,1,824),(498,'село Ударное',21,1,366),(499,'село Сосновка',21,1,188),(500,'село Автономовка',21,1,126),(501,'село Верхнеборовая',21,1,33),(502,'село Державинка',21,1,111),(503,'село Томское',21,1,1960),(504,'село Белогорка',21,1,332),(505,'село Бочкаревка',21,1,1046),(506,'село Красная Поляна',21,1,151),(507,'село Тавричанка',21,1,283),(508,'железнодорожная станция Украина',21,1,72),(509,'село Хитровка',21,1,114),(510,'село Украинка',21,1,1146),(511,'село Верное',21,1,123),(512,'село Новоохочье',21,1,104),(513,'село Фроловка',21,1,134),(514,'село Борисполь',21,1,206),(515,'село Широкий Лог',21,1,258),(516,'село Воскресеновка',21,1,58),(517,'село Соколовка',21,1,42),(518,'г. Сковородино',22,1,8943),(519,'посёлок Лесной',22,1,337),(520,'пгт Ерофей Павлович',22,1,4438),(521,'железнодорожная станция Большая Омутная',22,1,161),(522,'железнодорожный разъезд Аячи',22,1,24),(523,'железнодорожный разъезд Иташино',22,1,5),(524,'железнодорожный разъезд Ороченский',22,1,5),(525,'железнодорожный разъезд Сегачама',22,1,34),(526,'железнодорожный разъезд Текан',22,1,0),(527,'село Игнашино',22,1,168),(528,'населённый пункт Блок-Пост Ягодный',22,1,6),(529,'пгт Уруша',22,1,3262),(530,'железнодорожная станция Глубокий',22,1,2),(531,'населённый пункт Блок-Пост Ковали',22,1,1),(532,'железнодорожная станция Сгибеево',22,1,2),(533,'поселок  Улягир',22,1,1),(534,'железнодорожная станция Улятка',22,1,0),(535,'железнодорожная станция Халан',22,1,0),(536,'село Албазино',22,1,348),(537,'село Осежино',22,1,12),(538,'село Джалинда',22,1,1077),(539,'посёлок Среднерейновский',22,1,53),(540,'посёлок Таежный',22,1,46),(541,'село Невер',22,1,1357),(542,'железнодорожная станция Ульручьи',22,1,161),(543,'посёлок Солнечный',22,1,332),(544,'железнодорожная станция Бам',22,1,853),(545,'железнодорожная станция Имачи',22,1,0),(546,'село Талдан',22,1,2758),(547,'село  Тахтамыгда',22,1,1455),(548,'железнодорожная станция  Мадалан',22,1,353),(549,'поселок  Ольдой',22,1,21),(550,'село Жариково',23,1,588),(551,'село Свободка',23,1,169),(552,'село Козьмодемьяновка',23,1,1420),(553,'село Липовка',23,1,128),(554,'село Чуевка',23,1,179),(555,'село Лазаревка',23,1,295),(556,'село Куропатино',23,1,455),(557,'село Духовское',23,1,90),(558,'село Красное',23,1,247),(559,'село Корфово',23,1,73),(560,'село Лермонтовка',23,1,698),(561,'село Муравьевка',23,1,443),(562,'село Резуновка',23,1,190),(563,'село Николаевка',23,1,899),(564,'село Новоалександровка',23,1,1328),(565,'село Лиманное',23,1,151),(566,'село Раздольное',23,1,1719),(567,'село Гильчин',23,1,377),(568,'село Рощино',23,1,141),(569,'село Садовое',23,1,849),(570,'село Лозовое',23,1,793),(571,'село Орлецкое',23,1,206),(572,'село Тамбовка',23,1,7136),(573,'село Косицино',23,1,691),(574,'село Привольное',23,1,332),(575,'село Придорожное',23,1,520),(576,'село Толстовка',23,1,728),(577,'посёлок Аносовский',6,1,197),(578,'посёлок Беленький',6,1,132),(579,'посёлок Восточный',6,1,1131),(580,'посёлок Дипкун',6,1,1349),(581,'посёлок Кувыкта',6,1,268),(582,'посёлок Ларба',6,1,375),(583,'посёлок Лопча',6,1,382),(584,'посёлок Маревый',6,1,600),(585,'посёлок Могот',6,1,611),(586,'посёлок Лапри',6,1,6),(587,'посёлок Муртыгит',6,1,321),(588,'село Усть-Уркима',6,1,249),(589,'посёлок Олекма',6,1,443),(590,'село Первомайское',6,1,762),(591,'село Соловьевск',6,1,2664),(592,'посёлок Стрелка',6,1,1),(593,'село Янкан',6,1,54),(594,'посёлок Тутаул',6,1,389),(595,'село Уркан',6,1,747),(596,'село Бугорки',6,1,54),(597,'село Усть-Нюкжа',6,1,573),(598,'посёлок Хорогочи',6,1,331),(599,'посёлок Чильчи',6,1,207),(600,'посёлок Юктали',6,1,1167),(601,'железнодорожная станция Берея',7,1,65),(602,'село Малиновка',7,1,141),(603,'село Раздольное',7,1,44),(604,'село Мухино',7,1,801),(605,'село Ключевое',7,1,332),(606,'железнодорожная станция Переселенец',7,1,1),(607,'железнодорожная станция Ту',7,1,0),(608,'село Нововоскресеновка',7,1,490),(609,'село Аносово',7,1,98),(610,'село Новогеоргиевка',7,1,405),(611,'село Актай',7,1,107),(612,'село Свободный Труд',7,1,16),(613,'село Петруши',7,1,375),(614,'село Базисное',7,1,115),(615,'железнодорожная станция Петруши',7,1,28),(616,'село Случайное',7,1,0),(617,'село Саскаль',7,1,471),(618,'село Селеткан',7,1,270),(619,'железнодорожная станция Джатва',7,1,5),(620,'село Светильное',7,1,91),(621,'село Симоново',7,1,96),(622,'село Ураловка',7,1,179),(623,'село Кухтерин Луг',7,1,9),(624,'село Ушаково',7,1,463),(625,'село Чагоян',7,1,320);
/*!40000 ALTER TABLE `lacality` ENABLE KEYS */;
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
