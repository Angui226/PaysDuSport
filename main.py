import sqlite3
#import get_json_files

conn = sqlite3.connect('database.db') #creation de notre base de donnee
c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS Installation''')
c.execute('''DROP TABLE IF EXISTS Equipement''')
c.execute('''DROP TABLE IF EXISTS Activite''')


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
                                        

#test = c.execute('''SELECT * FROM Installation''')
#test = c.fetchone()
      
conn.commit()
conn.close()

#recuperation_json()