-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 19, 2020 at 04:58 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.3.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel_name`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `id` int(11) NOT NULL,
  `name` varchar(250) NOT NULL,
  `no_guest` int(250) NOT NULL,
  `room_type` varchar(250) NOT NULL,
  `checkin` varchar(250) NOT NULL,
  `checkout` varchar(250) NOT NULL,
  `hot_name` varchar(250) NOT NULL,
  `book_date` varchar(250) NOT NULL,
  `total` int(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`id`, `name`, `no_guest`, `room_type`, `checkin`, `checkout`, `hot_name`, `book_date`, `total`) VALUES
(1, 'Manas Singh', 2, 'Standard', '2020-09-19', '2020-09-21', 'manas', '2020-09-19', 200),
(2, 'Kamal', 10, 'Standard', '2020-09-25', '2020-09-30', 'Elango', '2020-09-25', 500);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_name`
--

CREATE TABLE `hotel_name` (
  `id` int(11) NOT NULL,
  `hotelname` varchar(250) NOT NULL,
  `deluxe_no` int(250) NOT NULL,
  `luxury_no` int(250) NOT NULL,
  `standard_no` int(250) NOT NULL,
  `image` varchar(250) NOT NULL,
  `description` varchar(250) NOT NULL,
  `sta_p` int(250) NOT NULL,
  `dex_p` int(250) NOT NULL,
  `lux_p` int(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hotel_name`
--

INSERT INTO `hotel_name` (`id`, `hotelname`, `deluxe_no`, `luxury_no`, `standard_no`, `image`, `description`, `sta_p`, `dex_p`, `lux_p`) VALUES
(4, 'Hotel Continental', 2, 2, 5, 'C:/Users/singh/Documents/GitHub/Dictionary/background1.jpg', 'Situated in Lucknow', 100, 500, 300),
(5, 'Elango Park', 5, 5, 5, 'C:/Users/singh/Documents/GitHub/Dictionary/background.jpg', 'Situated in chennai', 150, 250, 350),
(6, 'Hotel Xyz', 5, 5, 5, 'C:/Users/singh/Documents/GitHub/Dictionary/background1.jpg', 'Lovely Place', 120, 160, 260);

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(11) NOT NULL,
  `name` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `phone` bigint(250) NOT NULL,
  `pass` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `name`, `email`, `phone`, `pass`) VALUES
(1, 'Manas', 'singh.manas1708@gmail.com', 8707669520, '12345'),
(3, 'kamal', 'k@g.com', 0, '1234'),
(7, 'testing', 'test@gmail.com', 0, '123456');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hotel_name`
--
ALTER TABLE `hotel_name`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `hotel_name`
--
ALTER TABLE `hotel_name`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
