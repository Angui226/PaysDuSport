import sqlite3

def creation_table_database():
    conn = sqlite3.connect('database.db') #creation a notre base de donnee
    c = conn.cursor()
    #supprimer les tables si elles existent
    c.execute('''DROP TABLE IF EXISTS Installation''')
    c.execute('''DROP TABLE IF EXISTS Equipement''')
    c.execute('''DROP TABLE IF EXISTS Activite''')
    
    #creation des tables
    c.execute('''CREATE TABLE Installation (
                                            NumeroInstall INT PRIMARY KEY NOT NULL,
                                            Latitude VARCHAR(100),
                                            Longitude VARCHAR(100),
                                            CodePostal VARCHAR(5),
                                            Commune VARCHAR(100),
                                            Rue VARCHAR(255),
                                            Train BOOL,
                                            Bus BOOL,
                                            Tram BOOL
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
                                            CONSTRAINT fk_install_equipe
                                                FOREIGN KEY(NumeroEquipement)
                                                REFERENCES Equipement(NumeroEquipement)
                                            )''')
    conn.commit()
    conn.close()