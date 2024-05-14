-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: blogblend
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.22.04.1

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
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` text NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int NOT NULL,
  `post_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `post_id` (`post_id`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `like`
--

DROP TABLE IF EXISTS `like`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `like` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `user_id` int NOT NULL,
  `post_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `post_id` (`post_id`),
  CONSTRAINT `like_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  CONSTRAINT `like_ibfk_2` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `like`
--

LOCK TABLES `like` WRITE;
/*!40000 ALTER TABLE `like` DISABLE KEYS */;
/*!40000 ALTER TABLE `like` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cover` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `content` text NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `post_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (19,'f7deaaadee2cf41c.jpg','Post 1','Post number 1','2024-05-03 19:31:39','2024-05-07 22:00:40',4),(26,'3e3c9382715376f5.jpg','Test Article new','Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article Test Article ','2024-05-07 21:55:24','2024-05-11 16:44:16',5),(27,'bbbed9266826ca6e.jpg','New Article','A new Test Article','2024-05-07 21:59:04','2024-05-07 21:59:04',6),(28,'5d60d943472c6deb.jpg','Hello World!','Hello to web development world!','2024-05-07 21:59:58','2024-05-07 21:59:58',6),(29,'cf1491baf10c6117.jpg','10 Tips for Maintaining Productivity While Working Remotely','Introduction:\r\nIn recent years, remote work has become increasingly popular, offering flexibility and freedom for employees and employers alike. However, working from home comes with its own set of challenges, including maintaining productivity in a less structured environment. In this article, we\'ll explore ten practical tips to help you stay focused and productive while working remotely.\r\n\r\n1. Create a Dedicated Workspace:\r\nDesignate a specific area in your home for work, preferably away from distractions like the TV or high-traffic areas. Having a dedicated workspace helps signal to your brain that it\'s time to focus and get things done.\r\n\r\n2. Establish a Routine:\r\nSet regular working hours and stick to them as much as possible. Creating a routine can help you maintain structure and consistency in your day, making it easier to transition into work mode.\r\n\r\n3. Dress for Success:\r\nWhile it might be tempting to work in your pajamas, getting dressed as if you were going to the office can help put you in the right mindset for work. Dressing professionally can boost your confidence and productivity.\r\n\r\n4. Minimize Distractions:\r\nIdentify potential distractions in your environment and take steps to minimize them. This might involve turning off notifications, setting boundaries with family members, or using tools like noise-canceling headphones.\r\n\r\n5. Break Up Your Day:\r\nAvoid sitting at your desk for long periods without breaks. Instead, schedule regular short breaks throughout the day to rest and recharge. Use techniques like the Pomodoro Technique to work in focused bursts with built-in breaks.\r\n\r\n6. Set Clear Goals and Priorities:\r\nStart each day with a clear plan of what you want to accomplish. Break down your tasks into smaller, actionable steps and prioritize them based on importance and deadlines.\r\n\r\n7. Stay Connected with Colleagues:\r\nMaintain regular communication with your colleagues through tools like email, instant messaging, or video calls. Collaboration and social interaction are important for staying motivated and connected while working remotely.\r\n\r\n8. Practice Time Management:\r\nUse time management techniques like time blocking or the Eisenhower Matrix to prioritize tasks and allocate your time effectively. Set realistic goals and deadlines for yourself to stay on track.\r\n\r\n9. Get Moving:\r\nIncorporate physical activity into your daily routine to boost your energy levels and productivity. Take short walks, do quick workouts, or stretch regularly to combat the sedentary nature of remote work.\r\n\r\n10. Cultivate a Healthy Work-Life Balance:\r\nMaintain boundaries between work and personal life to prevent burnout. Set boundaries around your working hours and make time for hobbies, relaxation, and spending time with loved ones outside of work.\r\n\r\nConclusion:\r\nBy implementing these ten tips, you can create a productive and fulfilling remote work experience. Remember that finding what works best for you may require some trial and error, so don\'t be afraid to experiment with different strategies until you find the right balance for your needs.','2024-05-07 22:03:20','2024-05-11 15:32:47',5),(30,'1f542af5acd1e0b9.jpeg','The Rise of Artificial Intelligence in Everyday Life: How AI is Transforming Our World','Introduction:\r\nArtificial Intelligence (AI) has rapidly evolved from a concept of science fiction to a powerful and ubiquitous technology that permeates many aspects of our daily lives. In this article, we\'ll explore the growing influence of AI across various industries and examine its impact on everything from healthcare to entertainment.\r\n\r\n1. AI in Healthcare:\r\nDiscuss how AI is revolutionizing healthcare by enabling more accurate diagnostics, personalized treatment plans, and predictive analytics. Highlight examples such as AI-powered medical imaging, virtual health assistants, and drug discovery algorithms.\r\n\r\n2. AI in Finance:\r\nExplore how AI is reshaping the financial industry through applications like algorithmic trading, fraud detection, and personalized financial advice. Discuss the role of AI-powered chatbots in customer service and the use of machine learning for risk assessment and portfolio management.\r\n\r\n3. AI in Transportation:\r\nExamine the role of AI in transforming transportation systems, including self-driving cars, predictive maintenance for vehicles and infrastructure, and intelligent traffic management. Discuss the potential benefits of AI for improving safety, reducing congestion, and optimizing logistics.\r\n\r\n4. AI in Education:\r\nExplore how AI is enhancing education through adaptive learning platforms, personalized tutoring systems, and intelligent content creation tools. Discuss the potential of AI to improve student outcomes, increase access to education, and support lifelong learning.\r\n\r\n5. AI in Entertainment:\r\nDiscuss the ways in which AI is revolutionizing the entertainment industry, from recommendation algorithms on streaming platforms to AI-generated music and art. Explore how AI-powered content creation tools are democratizing creativity and pushing the boundaries of artistic expression.\r\n\r\n6. AI in Marketing:\r\nExamine how AI is transforming marketing and advertising through personalized messaging, predictive analytics, and customer segmentation. Discuss the use of AI-powered chatbots, virtual assistants, and recommendation engines to enhance the customer experience and drive sales.\r\n\r\n7. Ethical Considerations:\r\nAddress the ethical implications of AI technology, including concerns related to privacy, bias, and job displacement. Discuss the importance of responsible AI development and the need for ethical guidelines and regulations to ensure that AI benefits society as a whole.\r\n\r\n8. The Future of AI:\r\nSpeculate on the future of AI and its potential to further shape our world in the years to come. Discuss emerging trends such as reinforcement learning, quantum computing, and human-AI collaboration, and explore the possibilities and challenges that lie ahead.\r\n\r\nConclusion:\r\nAs AI continues to advance and integrate into our lives, it\'s clear that its impact will only continue to grow. By understanding the potential of AI and addressing its challenges responsibly, we can harness its power to drive innovation, improve efficiency, and enhance the human experience across all sectors of society.','2024-05-07 22:06:23','2024-05-07 22:06:23',6),(31,'8884f68361968425.jpg','Demystifying Blockchain: Understanding the Revolutionary Technology Behind Cryptocurrencies and Beyond','Introduction:\r\nBlockchain technology has garnered significant attention in recent years, largely due to its association with cryptocurrencies like Bitcoin. However, blockchain has far-reaching implications beyond digital currencies, with potential applications in various industries. In this article, we\'ll delve into the fundamentals of blockchain technology and explore its revolutionary potential.\r\n\r\n1. What is Blockchain?\r\nBegin by explaining the basic concept of blockchain: a decentralized, distributed ledger technology that records transactions across multiple computers in a tamper-proof and transparent manner. Discuss the key components of blockchain, including blocks, hashes, and consensus mechanisms.\r\n\r\n2. Cryptocurrencies and Blockchain:\r\nExplore the relationship between cryptocurrencies and blockchain technology. Discuss how blockchain serves as the underlying infrastructure for cryptocurrencies like Bitcoin and Ethereum, enabling secure and transparent peer-to-peer transactions without the need for intermediaries.\r\n\r\n3. Beyond Cryptocurrencies:\r\nExamine the diverse applications of blockchain technology beyond digital currencies. Highlight examples such as supply chain management, healthcare records management, identity verification, and voting systems. Discuss how blockchain can enhance transparency, security, and efficiency in various industries.\r\n\r\n4. Smart Contracts:\r\nIntroduce the concept of smart contracts, self-executing contracts with the terms of the agreement directly written into code. Discuss how smart contracts leverage blockchain technology to automate and enforce contractual agreements in a secure and decentralized manner.\r\n\r\n5. Challenges and Limitations:\r\nAcknowledge the challenges and limitations facing blockchain technology, including scalability issues, energy consumption concerns, regulatory uncertainty, and the potential for misuse. Discuss ongoing efforts to address these challenges and improve the scalability and sustainability of blockchain networks.\r\n\r\n6. Enterprise Adoption:\r\nExamine the growing interest in blockchain technology among enterprises and organizations. Discuss how businesses are exploring blockchain solutions for supply chain optimization, transparent supply chain management, and secure data sharing among stakeholders.\r\n\r\n7. The Future of Blockchain:\r\nSpeculate on the future of blockchain technology and its potential to transform industries and reshape the digital landscape. Discuss emerging trends such as interoperability between blockchain networks, decentralized finance (DeFi), and the integration of blockchain with other emerging technologies like artificial intelligence and the Internet of Things (IoT).\r\n\r\nConclusion:\r\nBlockchain technology has the potential to revolutionize industries, disrupt traditional business models, and empower individuals with greater control over their data and transactions. By understanding the fundamentals of blockchain and exploring its diverse applications, we can unlock the transformative power of this revolutionary technology for the benefit of society as a whole.','2024-05-07 22:08:37','2024-05-07 22:08:37',6),(33,'41dd9ff89615350e.jpg','The Impact of 5G Technology: Revolutionizing Connectivity and Transforming Industries','Introduction:\r\nWith the rollout of 5G technology gaining momentum around the world, there\'s a growing anticipation of its transformative potential. In this article, we\'ll explore the profound impact of 5G technology on connectivity, industries, and the way we live and work.\r\n\r\n1. Understanding 5G Technology:\r\nBegin by explaining what 5G technology is and how it differs from previous generations of wireless technology. Discuss its key features, including faster data speeds, lower latency, and increased network capacity, which enable a wide range of new applications and services.\r\n\r\n2. Enhanced Connectivity:\r\nExplore how 5G technology is revolutionizing connectivity by providing faster and more reliable internet access to users across various devices and locations. Discuss the implications of ultra-fast download and upload speeds for streaming, gaming, remote work, and IoT devices.\r\n\r\n3. Empowering IoT and Smart Cities:\r\nDiscuss how 5G technology is driving the proliferation of IoT devices and enabling the development of smart cities. Explore use cases such as smart infrastructure, connected vehicles, and real-time monitoring systems, which rely on 5G\'s high-speed, low-latency connectivity to function effectively.\r\n\r\n4. Transforming Industries:\r\nExamine the impact of 5G technology on various industries, including healthcare, manufacturing, transportation, and entertainment. Discuss how 5G enables innovations such as remote surgery, industrial automation, autonomous vehicles, and immersive experiences like augmented reality (AR) and virtual reality (VR).\r\n\r\n5. Edge Computing and Edge AI:\r\nExplore the synergy between 5G and edge computing, which brings computing resources closer to the end-users and IoT devices. Discuss how edge computing, combined with 5G\'s high-speed connectivity, enables real-time data processing and analysis, as well as the deployment of AI-powered applications at the network edge.\r\n\r\n6. Digital Divide and Inclusion:\r\nAddress concerns about the digital divide and the need to ensure equitable access to 5G technology for all communities. Discuss initiatives aimed at bridging the gap and empowering underserved populations through expanded connectivity and digital literacy programs.\r\n\r\n7. Security and Privacy Challenges:\r\nAcknowledge the security and privacy challenges associated with 5G technology, including concerns about data privacy, network vulnerabilities, and potential cyber threats. Discuss the importance of implementing robust security measures and regulatory frameworks to safeguard against risks.\r\n\r\n8. Global Adoption and Collaboration:\r\nExamine the global landscape of 5G adoption and collaboration among governments, telecommunications companies, and technology providers. Discuss the efforts to standardize 5G technology, allocate spectrum, and invest in infrastructure to support widespread deployment.\r\n\r\nConclusion:\r\nAs 5G technology continues to evolve and expand, its impact will be felt across industries and communities worldwide. By embracing the opportunities and addressing the challenges, we can harness the full potential of 5G to drive innovation, economic growth, and societal progress in the digital age.','2024-05-07 22:21:17','2024-05-07 22:21:17',7),(34,'8c79a564a416a60e.jpg','A test Post','A test post content','2024-05-07 22:29:27','2024-05-07 22:29:27',8);
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post_tag`
--

DROP TABLE IF EXISTS `post_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post_tag` (
  `post_id` int NOT NULL,
  `tag_id` int NOT NULL,
  PRIMARY KEY (`post_id`,`tag_id`),
  KEY `tag_id` (`tag_id`),
  CONSTRAINT `post_tag_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`) ON DELETE CASCADE,
  CONSTRAINT `post_tag_ibfk_2` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post_tag`
--

LOCK TABLES `post_tag` WRITE;
/*!40000 ALTER TABLE `post_tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `post_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tag`
--

DROP TABLE IF EXISTS `tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tag` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag`
--

LOCK TABLES `tag` WRITE;
/*!40000 ALTER TABLE `tag` DISABLE KEYS */;
INSERT INTO `tag` VALUES (1,'tag1'),(2,'tag2'),(3,'tag3'),(4,'tag4'),(5,'tech'),(6,'Hamo'),(7,'development'),(8,'jhvsdf');
/*!40000 ALTER TABLE `tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(80) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password` varchar(80) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `bio` varchar(255) DEFAULT NULL,
  `avatar` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (4,'Raafat','r@r.com','$2b$12$js8fYYbD1OhdZavGsWMKoO4u8s9L404R1LPWLTr4ItJGZmPRWAATW','2024-05-03 19:30:25','2024-05-03 19:30:25',NULL,'defaulte_profile.png'),(5,'mraafat','mraafat.elsayed@gmail.com','$2b$12$eVsvKNXqWx8Uuu9Z63iEaebqcShcgWR1gu6na/B9hdahgZ8XNEaE6','2024-05-04 16:38:19','2024-05-11 21:18:15','محمد رأفت','fe303b0f31900c46.jpeg'),(6,'John Doe','John@gmail.com','$2b$12$ivlgNHnbGht/IAFFt3.jyeXPp/HOYWEJiOPySRRPniWptyGrDj8xq','2024-05-07 21:58:06','2024-05-07 22:11:41','','bc6de15c19bebc91.jpeg'),(7,'Ahmed_S','ahmed@gmail.com','$2b$12$lGPM262cQP8ryYfMbCYTWuwF0FtLuMxHH3iA/ANu2grDD3nFyCyze','2024-05-07 22:19:25','2024-05-07 22:20:28','My name is Ahmed','c609b5a00402f140.jpg'),(8,'mraafat1','mraafat@gmail.com','$2b$12$Cvlj6LJTOqnN3aYjippCP.R762/Iq9IboaScaHCN2Gt14AMPwktMe','2024-05-07 22:26:49','2024-05-07 22:29:05','My name i Mohamed Raafat','85423b786353fcd7.jpg'),(9,'Raafat2','raafat2@raafat.com','$2b$12$dMi8iOSaaaI.ckq5w8Xfsewt4VNwyeuU3E91B.jsj8fBGFbMnUWny','2024-05-11 15:22:30','2024-05-11 15:23:28','My name is Raafat2','33b188a4f859d50d.jpg'),(10,'123456','12345@12345.com','$2b$12$zgXRuLSravEAwNvPMeh0Ne8x/9UUDkMAaUlkDvbL6VRWaI30vcwMG','2024-05-11 16:45:04','2024-05-11 17:00:50','12345','06f64761c191b867.jpg');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-14 20:37:42
