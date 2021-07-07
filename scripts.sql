--SCRIPTS AS PER MYSQL NEEDS TO BE CHANGED
CREATE DATABASE IF NOT EXISTS `bikewise_db`;
CREATE TABLE `bikewise_data` (
  `id` bigint NOT NULL,
  `title` text,
  `description` text,
  `address` text,
  `occurred_at` bigint DEFAULT NULL,
  `updated_at` bigint DEFAULT NULL,
  `url` text,
  `location_type` text,
  `location_description` text,
  `type` text,
  `type_properties` text,
  `source_name` text,
  `source_html_url` text,
  `source_api_url` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;