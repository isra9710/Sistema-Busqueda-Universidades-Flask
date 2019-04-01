-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 01, 2019 at 06:24 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `base`
--

-- --------------------------------------------------------

--
-- Table structure for table `Administrador`
--

CREATE TABLE `Administrador` (
  `id_administrador` int(11) NOT NULL,
  `nombre_admin` varchar(50) NOT NULL,
  `contra_admin` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Administrador`
--

INSERT INTO `Administrador` (`id_administrador`, `nombre_admin`, `contra_admin`) VALUES
(1, 'Israel', '123'),
(2, 'Rod', '123');

-- --------------------------------------------------------

--
-- Table structure for table `Calificacion`
--

CREATE TABLE `Calificacion` (
  `id_calificacion` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_universidad` int(11) NOT NULL,
  `calificacion` float NOT NULL,
  `comentarios` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Calificacion`
--

INSERT INTO `Calificacion` (`id_calificacion`, `id_usuario`, `id_universidad`, `calificacion`, `comentarios`) VALUES
(1, 1, 2, 3, 'Muy buena');

-- --------------------------------------------------------

--
-- Table structure for table `Carrera`
--

CREATE TABLE `Carrera` (
  `id_carrera` int(11) NOT NULL,
  `id_universidad` int(11) NOT NULL,
  `puntuacion_carrera` float NOT NULL,
  `nombre_carrera` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Taller`
--

CREATE TABLE `Taller` (
  `id_talleres` int(11) NOT NULL,
  `id_universidad` int(11) NOT NULL,
  `nombre_taller` varchar(45) NOT NULL,
  `tipo_taller` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Taller`
--

INSERT INTO `Taller` (`id_talleres`, `id_universidad`, `nombre_taller`, `tipo_taller`) VALUES
(12, 2, 'Judo', 'Deportivo'),
(13, 2, 'Box', 'Cultural');

-- --------------------------------------------------------

--
-- Table structure for table `Universidad`
--

CREATE TABLE `Universidad` (
  `id_universidad` int(11) NOT NULL,
  `id_administrador` int(11) NOT NULL,
  `nombre_universidad` varchar(50) DEFAULT NULL,
  `promedio` float NOT NULL,
  `paginaWeb` varchar(300) NOT NULL,
  `foto` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Universidad`
--

INSERT INTO `Universidad` (`id_universidad`, `id_administrador`, `nombre_universidad`, `promedio`, `paginaWeb`, `foto`) VALUES
(2, 1, 'IPN', 3, 'https://www.ipn.mx/', ''),
(4, 1, 'Upemor', 7, 'https://www.upemor.edu.mx/', ''),
(5, 1, 'ITZ', 5.6, 'http://www.itzacatepec.edu.mx/', ''),
(8, 1, 'UVM', 0, 'https://uvm.mx/campus-cuernavaca', 'Logo-UVM-1.jpg'),
(9, 2, 'UAEM', 7.8, 'https://www.uaem.mx/', 'BoGfX5gA_400x400.jpg'),
(10, 2, 'ULA', 0, 'https://www.uaem.mx/', 'ula181630thumbnail.png');

-- --------------------------------------------------------

--
-- Table structure for table `Usuario`
--

CREATE TABLE `Usuario` (
  `id_usuario` int(11) NOT NULL,
  `id_universidad` int(11) NOT NULL,
  `nombre_usuario` varchar(50) NOT NULL,
  `contra_usuario` varchar(50) NOT NULL,
  `calificar` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Usuario`
--

INSERT INTO `Usuario` (`id_usuario`, `id_universidad`, `nombre_usuario`, `contra_usuario`, `calificar`) VALUES
(1, 2, 'isra.rios.con@gmail.com', '123', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Administrador`
--
ALTER TABLE `Administrador`
  ADD PRIMARY KEY (`id_administrador`);

--
-- Indexes for table `Calificacion`
--
ALTER TABLE `Calificacion`
  ADD PRIMARY KEY (`id_calificacion`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_universidad` (`id_universidad`);

--
-- Indexes for table `Carrera`
--
ALTER TABLE `Carrera`
  ADD PRIMARY KEY (`id_carrera`),
  ADD KEY `id_universidad` (`id_universidad`);

--
-- Indexes for table `Taller`
--
ALTER TABLE `Taller`
  ADD PRIMARY KEY (`id_talleres`),
  ADD KEY `id_universidad` (`id_universidad`);

--
-- Indexes for table `Universidad`
--
ALTER TABLE `Universidad`
  ADD PRIMARY KEY (`id_universidad`),
  ADD KEY `id_administrador` (`id_administrador`);

--
-- Indexes for table `Usuario`
--
ALTER TABLE `Usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD KEY `id_universidad` (`id_universidad`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Administrador`
--
ALTER TABLE `Administrador`
  MODIFY `id_administrador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `Calificacion`
--
ALTER TABLE `Calificacion`
  MODIFY `id_calificacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `Carrera`
--
ALTER TABLE `Carrera`
  MODIFY `id_carrera` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Taller`
--
ALTER TABLE `Taller`
  MODIFY `id_talleres` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `Universidad`
--
ALTER TABLE `Universidad`
  MODIFY `id_universidad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `Usuario`
--
ALTER TABLE `Usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Calificacion`
--
ALTER TABLE `Calificacion`
  ADD CONSTRAINT `Calificacion_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `Usuario` (`id_usuario`),
  ADD CONSTRAINT `Calificacion_ibfk_2` FOREIGN KEY (`id_universidad`) REFERENCES `Universidad` (`id_universidad`);

--
-- Constraints for table `Carrera`
--
ALTER TABLE `Carrera`
  ADD CONSTRAINT `Carrera_ibfk_1` FOREIGN KEY (`id_universidad`) REFERENCES `Universidad` (`id_universidad`);

--
-- Constraints for table `Taller`
--
ALTER TABLE `Taller`
  ADD CONSTRAINT `Taller_ibfk_1` FOREIGN KEY (`id_universidad`) REFERENCES `Universidad` (`id_universidad`);

--
-- Constraints for table `Universidad`
--
ALTER TABLE `Universidad`
  ADD CONSTRAINT `Universidad_ibfk_1` FOREIGN KEY (`id_administrador`) REFERENCES `Administrador` (`id_administrador`);

--
-- Constraints for table `Usuario`
--
ALTER TABLE `Usuario`
  ADD CONSTRAINT `Usuario_ibfk_1` FOREIGN KEY (`id_universidad`) REFERENCES `Universidad` (`id_universidad`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
