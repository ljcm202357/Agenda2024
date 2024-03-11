-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-03-2024 a las 12:57:12
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `agenda2024`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personas`
--

CREATE TABLE `personas` (
  `idper` int(11) NOT NULL,
  `nombreper` varchar(60) NOT NULL,
  `apellidoper` varchar(60) NOT NULL,
  `emailper` varchar(60) NOT NULL,
  `dirper` varchar(60) NOT NULL,
  `telper` varchar(60) NOT NULL,
  `usuarioper` varchar(60) NOT NULL,
  `contraper` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `personas`
--

INSERT INTO `personas` (`idper`, `nombreper`, `apellidoper`, `emailper`, `dirper`, `telper`, `usuarioper`, `contraper`) VALUES
(1, 'Luisa Fernanda', 'Martinez', 'martinez2024@gmail.com', 'versalles', '2698745', '', '123456789'),
(2, 'Hamet Daniel', 'Vega', 'vega2024@gmail.com', 'sena', '3698574', '', '123456789'),
(3, 'Nicolas', 'Gomez', 'gomez0903@gmail.com', 'sena', '6987854', 'gomez2024', '789456123'),
(4, 'Ingrid Tatiana', 'Cifuentes Martinez', 'tata0930@gmail.com', 'bogota', '3121011', '', '123456789'),
(5, 'Luisa Fernanda', 'martinez martinez', 'ggm@gmail.com', 'cali', '7845965', 'ljcm293', '789456123');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `personas`
--
ALTER TABLE `personas`
  ADD PRIMARY KEY (`idper`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `personas`
--
ALTER TABLE `personas`
  MODIFY `idper` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
