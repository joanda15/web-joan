-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Aug 07, 2024 at 05:25 PM
-- Server version: 10.5.20-MariaDB
-- PHP Version: 7.3.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `id22330649_dbjogosa`
--

-- --------------------------------------------------------

--
-- Table structure for table `opiniones`
--

CREATE TABLE `opiniones` (
  `id` int(11) NOT NULL,
  `emailUser` varchar(150) NOT NULL,
  `opinion` text NOT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `opiniones`
--

INSERT INTO `opiniones` (`id`, `emailUser`, `opinion`, `created_at`) VALUES
(1, 'jdgs.1505@gmail.com', 'Hola', '2024-06-20 00:47:27'),
(2, 'jdgs.1505@gmail.com', 'Cel', '2024-06-20 00:48:14'),
(3, 'jdgs.1505@gmail.com', 'el chi', '2024-07-01 03:21:04'),
(4, 'jdgs.1505@gmail.com', 'Re', '2024-07-01 03:21:48'),
(5, 'jdgs.1505@gmail.com', 'Hola', '2024-07-03 04:14:24'),
(6, 'jdgs.1505@gmail.com', 'Se ve super papi', '2024-07-12 21:55:03');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `opiniones`
--
ALTER TABLE `opiniones`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `opiniones`
--
ALTER TABLE `opiniones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
