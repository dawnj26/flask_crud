-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 26, 2024 at 08:05 AM
-- Server version: 11.6.2-MariaDB
-- PHP Version: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask_endterm`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `stock` int(10) UNSIGNED NOT NULL,
  `category` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `name`, `description`, `price`, `stock`, `category`, `status`) VALUES
(1, 'Product 1', 'Description for product 1', 10.99, 100, 'Category A', 'available'),
(2, 'Product 2', 'Description for product 2', 15.49, 50, 'Category B', 'available'),
(3, 'Product 3', 'Description for product 3', 8.25, 0, 'Category A', 'out of stock'),
(4, 'Product 4', 'Description for product 4', 25.00, 10, 'Category C', 'out of stock'),
(5, 'Product 5', 'Description for product 5', 12.75, 80, 'Category B', 'available'),
(6, 'Product 6', 'Description for product 6', 18.99, 5, 'Category A', 'low stock'),
(7, 'Product 7', 'Description for product 7', 22.50, 0, 'Category C', 'out of stock'),
(8, 'Product 8', 'Description for product 8', 9.99, 120, 'Category B', 'available'),
(10, 'Product 10', 'Description for product 10', 30.00, 0, 'Category C', 'out of stock');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email_address` varchar(255) NOT NULL,
  `pwd` text NOT NULL,
  `phone_number` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `first_name`, `last_name`, `email_address`, `pwd`, `phone_number`, `address`) VALUES
(1, 'Donn Jayson', 'Quinto', 'dquinto@gmail.com', 'scrypt:32768:8:1$XPAC7Qu0W5CpKcKH$c849df2298244e02c080ea68ff25cdb67732ec0481bf1e6da88e3f4002431a1e56d2947a17b6f03504a4299ac25b16ebf7bc7a55b9250af4385f7f0d98294201', '09560575513', 'Bayambang, Pangasinan');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
