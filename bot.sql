-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 01, 2023 at 07:09 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bot`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `student_id` int(11) DEFAULT NULL,
  `month` varchar(255) DEFAULT NULL,
  `attendance` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bus_timings`
--

CREATE TABLE `bus_timings` (
  `id` int(11) NOT NULL,
  `bus_number` varchar(255) NOT NULL,
  `departure_time` time DEFAULT NULL,
  `arrival_time` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bus_timings`
--

INSERT INTO `bus_timings` (`id`, `bus_number`, `departure_time`, `arrival_time`) VALUES
(1, '161', '09:30:00', '10:30:00'),
(2, '161k', '10:30:00', '11:30:00'),
(3, '161', '00:00:00', '00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `student_attendance`
--

CREATE TABLE `student_attendance` (
  `id` int(11) NOT NULL,
  `date` date NOT NULL,
  `student_id` int(11) NOT NULL,
  `status` enum('present','absent','late') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student_attendance`
--

INSERT INTO `student_attendance` (`id`, `date`, `student_id`, `status`) VALUES
(1, '2023-04-27', 1, 'present');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('studentslogin','lecturerslogin') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `role`) VALUES
(1, 'Bharath', 'Bharath123', 'studentslogin'),
(2, 'Mahesh', 'Mahesh123', 'lecturerslogin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bus_timings`
--
ALTER TABLE `bus_timings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `student_attendance`
--
ALTER TABLE `student_attendance`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bus_timings`
--
ALTER TABLE `bus_timings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `student_attendance`
--
ALTER TABLE `student_attendance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
