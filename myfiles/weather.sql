-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Час генерацыі: 03 Тра 2023, 22:37
-- Версія сервера: 10.4.27-MariaDB
-- Вэрсія PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База даных: `networks6`
--

-- --------------------------------------------------------

--
-- Структура табліцы `weather`
--

CREATE TABLE `weather` (
  `Day` int(11) NOT NULL,
  `City` varchar(250) NOT NULL,
  `Temp` int(100) NOT NULL,
  `Date` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп дадзеных табліцы `weather`
--

INSERT INTO `weather` (`Day`, `City`, `Temp`, `Date`) VALUES
(1, 'Minsk', 30, '3 may'),
(2, 'Minsk', 20, '4 may'),
(3, 'Minsk', 13, '5 may'),
(4, 'Minsk', 13, '5 may'),
(5, 'Minsk', 18, '9 may');

--
-- Індэксы для захаваных табліц
--

--
-- Індэксы табліцы `weather`
--
ALTER TABLE `weather`
  ADD PRIMARY KEY (`Day`);

--
-- AUTO_INCREMENT для захаваных табліц
--

--
-- AUTO_INCREMENT для табліцы `weather`
--
ALTER TABLE `weather`
  MODIFY `Day` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
