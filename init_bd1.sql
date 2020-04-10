DROP database IF EXISTS bd_universitaire;
CREATE DATABASE bd_universitaire;
USE bd_universitaire;

CREATE TABLE Etudiant(
	idul smallint PRIMARY KEY,
	nom varchar(100),
	motDePasse varchar(40),
	motivation smallint,
	credit smallint,
	sigleProgramme varchar(100) NOT NULL UNIQUE,
	FOREIGN KEY(sigleProgramme) REFERENCES Programme(sigleProgramme) ON DELETE CASCADE
	);

CREATE TABLE Programme(
	sigleProgramme varchar(100) PRIMARY KEY,
    nom varchar(100),
	credit smallint
	);

	
CREATE TABLE Service(
	id smallint PRIMARY KEY,
	nom char(40),
    disponible smallint(1),
    sigleProgramme smallint NOT NULL,
    FOREIGN KEY(sigleProgramme) REFERENCES Programme(sigleProgramme) ON DELETE CASCADE
	);
    
CREATE TABLE Directeur(
	mail smallint ,
	nom char(40),
	numeroTelephone smallint,
    sigleProgramme smallint,
    PRIMARY KEY(mail, sigleProgramme),
    FOREIGN KEY(sigleProgramme) REFERENCES Programme(sigleProgramme) ON DELETE CASCADE #Modelisation de la relation possede un directeur
	);
    
CREATE TABLE Objectif(
	id smallint AUTO_INCREMENT,
	sessions varchar(100),
	nom char(40),
	moyenneSession smallint,
    moyenneFinProgramme smallint,
    moyenneCours smallint,
    idul varchar(100) NOT NULL,
    PRIMARY KEY(id), 
    FOREIGN KEY(idul) REFERENCES Programme(idul) ON DELETE CASCADE #modelisation de la relation posseder
	);

CREATE TABLE Cours(
	sigleCours smallint PRIMARY KEY,
	nom char(40),
	credit smallint,
    evaluation smallint
	);

CREATE TABLE Suivre(
	idul smallint,
    sigleCours smallint,
    sessions smallint,
	moyenne smallint,
    PRIMARY KEY(idul,  sigleCours),
    FOREIGN KEY(idul) REFERENCES Programme(idul),
    FOREIGN KEY(sigleCours) REFERENCES Cours(sigleCours)
	);
INSERT INTO Etudiant(idul, nom, motDePasse, motivation, credit, sigleProgramme)
	VALUE
	('DIBAX', 'Baxter Dieter', 'jsbvssdsd', 1, 0, GLO);
INSERT INTO Programme(sigleProgramme, nom,  credit)
	VALUE
	('GLO', 'Genie Logiciel', 120);
INSERT INTO Service(id, nom, disponible, sigleProgramme)
	VALUE
	(12345, 'CDA',1, 'GLO');
INSERT INTO directeur(mail, nom, numeroTelephone, sigleProgramme)
	VALUE
	('Brahim.Chaib-draa@ift.ulaval.ca',  'Brahim Chaib-draa', 4186562131, 'GLO');
INSERT INTO Objectif(id, session, nom, moyenneSession, moyenneFinProgramme, moyenneCours, idul)
	VALUE
	(2,  'Hiver', 'Tout Peter', 3, 3.45, 4, 'GLO');
INSERT INTO Cours(id, session, nom, moyenneSession, moyenneFinProgramme, moyenneCours, idul)
	VALUE
	(2,  'Hiver', 'Tout Peter', 3, 3.45, 4, 'GLO');

/*
CREATE TABLE Emprunts(
	cote smallint,
	pret date,
	retour date,
	id smallint,
	PRIMARY KEY(cote, pret),
	FOREIGN KEY(cote) REFERENCES Copies(cote) ON DELETE CASCADE,
	FOREIGN KEY(id) REFERENCES Utilisateurs(id) ON DELETE CASCADE
	);

INSERT INTO Suivre(id, session, nom, moyenneSession, moyenneFinProgramme, moyenneCours, idul)
	VALUE
	(2,  'Hiver', 'Tout Peter', 3, 3.45, 4, 'GLO');
	
INSERT INTO Copies(cote, isbn, disponible)
	VALUE
	(0, 1234, 1),
	(1, 1234, 0),
	(2, 1234, 0),
	(3, 2345, 0),
	(5, 4567, 1),
	(6, 5678, 0),
	(7, 5678, 0),
	(8, 6789, 1),
	(9, 7890, 0);
	
INSERT INTO Utilisateurs(id, nom, adresse, age)
	VALUE
	(10, 'Alice', '2020 Rue Finfin', 25),
	(20, 'Bob', '1111 Premiere Avenue', 7),
	(30, 'Cedric', '42 Rue de la Reponse', 15),
	(40, 'Denise', '1234 Avenue Croissante', 43),
	(50, 'Frank', '3 Carre du Pentagone', 5),
	(60, 'Gerard', '2020 Rue Finfin', 32),
	(70, 'Henry', '39 Avenue Khoury', 12);
	
INSERT INTO Emprunts (cote, pret, retour, id)
	VALUE
	(0, '2017-01-05', '2017-02-07', 10),
	(0, '2017-05-18', '2017-06-19', 30),
	(0, '2018-11-15', '2018-12-18', 50),
	(1, '2015-02-04', '2015-04-01', 10),
	(1, '2015-06-08', '2015-08-02', 20),
	(1, '2016-04-01', '2016-05-13', 40),
	(1, '2017-03-15', '2017-08-02', 30),
	(1, '2018-11-14', '2018-12-06', 70),
	(1, '2018-12-20', '2019-02-13', 60),
	(2, '2017-05-04', '2017-06-08', 50),
	(2, '2018-06-03', '2018-09-12', 30),
	(2, '2018-11-15', '2018-12-09', 60),
	(3, '2019-01-14', '2019-03-15', 60),
	(4, '2014-02-13', '2014-05-18', 40),
	(5, '2015-03-12', '2015-05-17', 10),
	(6, '2015-04-12', '2015-06-17', 30),
	(6, '2016-06-19', '2016-06-21', 20),
	(6, '2018-12-15', '2019-01-17', 70),
	(7, '2018-09-18', '2018-11-10', 50),
	(7, '2019-02-14', '2019-03-15', 20),
	(8, '2017-05-04', '2017-06-19', 30),
	(9, '2018-09-15', '2018-11-16', 60),
	(9, '2017-04-16', '2017-05-12', 10);
    fgoshgiuhteaiugh
    */