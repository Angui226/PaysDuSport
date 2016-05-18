#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

def creation_table_database():
    """
    Create the database if it doesn't exists, connect to it if it does.
    Drop table to avoid error
    create table with the correct variables
    """
    conn = sqlite3.connect('../db/database.db') #creation a notre base de donnee
    c = conn.cursor()
    #supprimer les tables si elles existent
    c.execute('''DROP TABLE IF EXISTS Installation''')
    c.execute('''DROP TABLE IF EXISTS Equipement''')
    c.execute('''DROP TABLE IF EXISTS Activite''')


    #creation des tables
    c.execute('''CREATE TABLE Installation (
                                            NumeroInstall INT PRIMARY KEY NOT NULL,
                                            Nom VARCHAR(255),
                                            Latitude VARCHAR(100),
                                            Longitude VARCHAR(100),
                                            CodePostal VARCHAR(5),
                                            Commune VARCHAR(100),
                                            Rue VARCHAR(255),
                                            Train VARCHAR(3),
                                            Bus VARCHAR(3),
                                            Tram VARCHAR(3)
                                            )''')
    c.execute('''CREATE TABLE Equipement (
                                            NumeroEquipement INT PRIMARY KEY NOT NULL,
                                            NumeroInstallation INT,
                                            NatureLibelle VARCHAR(100),
                                            InsNom VARCHAR(100),
                                            CONSTRAINT fk_install_equipe
                                                FOREIGN KEY(NumeroInstallation)
                                                REFERENCES Installation(NumeroInstall)
                                            )''')

    c.execute('''CREATE TABLE Activite (
                                            NumeroEquipement INT ,
                                            LibelleActivite VARCHAR(100),
                                            LibelleNiveau VARCHAR(100),
                                            Commune VARCHAR(100),
                                            CONSTRAINT fk_install_equipe
                                                FOREIGN KEY(NumeroEquipement)
                                                REFERENCES Equipement(NumeroEquipement)
                                            )''')

    conn.commit()
    conn.close()



def select_install_town( town, sport ):
    """
    select all equipement with given sport of a given town
    """
    conn = sqlite3.connect('../db/database.db') #creation a notre base de donnee
    c = conn.cursor()

    selectQuery = "SELECT DISTINCT i.NumeroInstall, i.Rue, i.Commune, i.Nom, a.LibelleActivite FROM INSTALLATION i, EQUIPEMENT e, ACTIVITE a  WHERE i.Commune = '"+town+"' AND a.LibelleActivite = '"+sport+"' AND e.NumeroEquipement = a.NumeroEquipement AND e.NumeroInstallation = i.NumeroInstall "


    c.execute( selectQuery )
    result = c.fetchall();

    conn.close()
    return result

def select_install_town_empty_town(sport):
    """
    select all cities where a sport is practiced
    """
    conn = sqlite3.connect('../db/database.db') #connect to database
    c = conn.cursor()

    selectQuery = "SELECT DISTINCT i.NumeroInstall, i.Rue, i.Commune, i.Nom, a.LibelleActivite FROM INSTALLATION i, EQUIPEMENT e, ACTIVITE a  WHERE a.LibelleActivite = '"+sport+"' AND e.NumeroEquipement = a.NumeroEquipement AND e.NumeroInstallation = i.NumeroInstall "


    c.execute( selectQuery )
    result = c.fetchall();

    conn.close()
    return result

def select_install_town_empty_sport(town):
    """
    select all equipement of a given town
    """
    conn = sqlite3.connect('../db/database.db') #connect to database
    c = conn.cursor()

    selectQuery = "SELECT DISTINCT i.NumeroInstall, i.Rue, i.Commune, i.Nom, a.LibelleActivite FROM INSTALLATION i, EQUIPEMENT e, ACTIVITE a  WHERE i.Commune = '"+town+"' AND e.NumeroEquipement = a.NumeroEquipement AND e.NumeroInstallation = i.NumeroInstall "

    c.execute( selectQuery )
    result = c.fetchall();

    conn.close()
    return result

def select_install_town_empty_all():
    """
    select all equipement of a given town
    """
    conn = sqlite3.connect('../db/database.db') #connect to database
    c = conn.cursor()

    selectQuery = "SELECT DISTINCT i.NumeroInstall, i.Rue, i.Commune, i.Nom, a.LibelleActivite FROM INSTALLATION i, EQUIPEMENT e, ACTIVITE a  WHERE e.NumeroEquipement = a.NumeroEquipement AND e.NumeroInstallation = i.NumeroInstall "

    c.execute( selectQuery )
    result = c.fetchall();

    conn.close()
    return result



def get_list_activites():
    """
    select all activities
    """
    conn = sqlite3.connect('../db/database.db') #connect to database
    c = conn.cursor()

    selectQuery = "SELECT DISTINCT a.LibelleActivite FROM ACTIVITE a ORDER BY a.LibelleActivite asc "


    c.execute( selectQuery )
    result = c.fetchall();

    conn.close()
    return result

def get_list_activites_changed(town):
    """
    select all activities
    """
    conn = sqlite3.connect('../db/database.db') #connect to database
    c = conn.cursor()

    selectQuery = "SELECT DISTINCT a.LibelleActivite FROM ACTIVITE a WHERE a.Commune ='"+town+"' ORDER BY a.LibelleActivite asc "


    c.execute( selectQuery )
    result = c.fetchall();

    conn.close()
    return result


def get_list_town():
    """
    select all town
    """
    conn = sqlite3.connect('../db/database.db') #connect to database
    c = conn.cursor()

    selectQuery = "SELECT DISTINCT a.Commune FROM ACTIVITE a ORDER BY a.Commune asc "


    c.execute( selectQuery )
    result = c.fetchall();

    conn.close()
    return result



#get specific installation
def get_specific_installation(id_activity):
    """
    return specific installation
    """
    conn = sqlite3.connect('../db/database.db') #connect to database
    c = conn.cursor()

    selectQuery = "SELECT * FROM INSTALLATION i WHERE NumeroInstall ="+id_activity


    c.execute( selectQuery )
    result = c.fetchall();

    conn.close()
    return result