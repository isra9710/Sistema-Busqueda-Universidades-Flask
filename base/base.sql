create database base;
use base;
create table Administrador(id_administrador int not null primary key auto_increment,nombre_admin varchar(50) not null,contra_admin varchar(50) not null
)engine=InnoDB;


create table Universidad(
  id_universidad int not null primary key auto_increment,id_administrador int not null,foreign key (id_administrador) references Administrador(id_administrador),nombre_universidad varchar(50),promedio float not null
)engine=InnoDB;

create table Carrera(
  id_carrera int not null primary key auto_increment ,id_universidad int not null,foreign key (id_universidad) references Universidad(id_universidad), puntuacion_carrera float not null, nombre_carrera varchar(50) not null
)engine=InnoDb;
CREATE TABLE Taller (
  id_talleres INT NOT NULL primary key AUTO_INCREMENT ,
  id_universidad INT NOT NULL,FOREIGN KEY (id_universidad)
  REFERENCES Universidad (id_universidad),
  nombre_taller VARCHAR(45) NOT NULL)
ENGINE = InnoDB;
create table Usuario(id_usuario int not null primary key auto_increment,id_universidad int not null,foreign key (id_universidad) references Universidad(id_universidad), nombre_usuario varchar(50) not null, contra_usuario varchar(50) not null)engine=InnoDB;

create table Calificacion(id_calificacion int not null primary key auto_increment,id_usuario int not null, foreign key (id_usuario) references Usuario(id_usuario),id_universidad int not null, foreign key(id_universidad) references Universidad(id_universidad),calificacion float not null, comentarios varchar(255) null )engine=InnoDB;
