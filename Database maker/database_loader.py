# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 00:02:28 2021

@author: eugen
"""

import mysql.connector
import os

def cortaCadenaHasta(cadena, hasta):
    res = 0
    while res<len(cadena):
        if cadena[res] == hasta:
            return res
        res = res +1
    return res


def getGames(archivo):
    f = open(archivo, "r")
    lines = f.readlines()
    
    result = {}
    indice = 0
    contraindice = 0
    resultaux = {}
    resultGame = ""
    
    for line in lines:
        if line[0] == "[":
            if contraindice == 1:
                contraindice = 0
                resultaux["Game"] = resultGame
                result[indice] = resultaux
                resultaux={}
                resultGame = ""
                indice = indice + 1
                
                
            aux = cortaCadenaHasta(line[1::], " ")
            aux2 = cortaCadenaHasta(line[aux+3::], '"')
            resultaux[line[1:aux+1]] = line[aux+3:aux + 2 + aux2 + 1]
            
        else:
            if contraindice == 0:
                contraindice = 1
            else:
                resultGame = resultGame + str(line)
    return result

def createTableGames(games):
    mydb = mysql.connector.connect(host="localhost",port=3306,user="root",database="alphaupo")
    mycursor = mydb.cursor()

    
    consulta = "INSERT INTO `partida` (`Id`, `Black`, `BlackElo`, `Date`, `ECO`, `Event`, `Game`, `Result`, `Round`, `Site`, `White`, `WhiteElo`) VALUES "
    
    i=0
    while i < len(games):
        
        if "Black" in games[i]:
            black = games[i]["Black"]
        else:
            black = ""
        
        if "BlackElo" in games[i]:
            blackElo = games[i]["BlackElo"]
        else:
            blackElo = ""
        
        if "Date" in games[i]:
            fecha = games[i]["Date"]
        else:
            fecha = ""
            
        if "ECO" in games[i]:
            eco = games[i]["ECO"]
        else:
            eco = ""
        
        if "Event" in games[i]:
            evento = games[i]["Event"]
        else:
            evento = ""
            
        if "Game" in games[i]:
            partida = games[i]["Game"]
        else:
            partida = ""
            
        if "Result" in games[i]:
            result = games[i]["Result"]
        else:
            result = ""
            
        if "Round" in games[i]:
            ronda = games[i]["Round"]
        else:
            ronda = ""
            
        if "Site" in games[i]:
            site = games[i]["Site"]
        else:
            site = ""
            
        if "White" in games[i]:
            white = games[i]["White"]
        else:
            white = ""
            
        if "WhiteElo" in games[i]:
            whiteElo = games[i]["WhiteElo"]
        else:
            whiteElo = ""
        
        if ((i+1) % 500) == 0:
            print("    " + str(int(((i+1) / len(games))*100))+"%")
            
            
            consulta = consulta[:-1]
            mycursor.execute(consulta)
            mydb.commit()
            
            consulta = "INSERT INTO `partida` (`Id`, `Black`, `BlackElo`, `Date`, `ECO`, `Event`, `Game`, `Result`, `Round`, `Site`, `White`, `WhiteElo`) VALUES "
            
            
        
        consulta = consulta + '(NULL, "'+ black +'", "'+ blackElo +'", "'+ fecha +'", "'+ eco +'", "'+ evento +'", "'+ partida +'", "'+ result +'", "'+ ronda +'", "'+ site +'", "'+ white +'", "'+ whiteElo +'"),'
        i = i +1
        
    consulta = consulta[:-1]
    mycursor.execute(consulta)
    mydb.commit()
    
    mycursor.close()
    mydb.close()
    
    print("    " + str(int(((i) / len(games))*100))+"%")
        
    
def getFiles(directorio):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(directorio):
        for file in f:
            if '.pgn' in file:
                files.append(os.path.join(r, file))
    
    return files


def deleteTables():
    mydb = mysql.connector.connect(host="localhost",port=3306,user="root",database="alphaupo")
    mycursor = mydb.cursor()

    
    
    consulta = "DROP TABLE IF EXISTS partida;"
    mycursor.execute(consulta)
    
    
    consulta = "CREATE TABLE `alphaupo`.`partida` ( `Id` INT NOT NULL AUTO_INCREMENT , `Black` VARCHAR(255), `BlackElo` INT, `Date` DATE, `ECO` VARCHAR(255), `Event` VARCHAR(255) , `Game` VARCHAR(4096) , `Result` VARCHAR(255), `Round` INT, `Site` VARCHAR(255), `White` VARCHAR(255) , `WhiteElo` INT , PRIMARY KEY (`Id`)) ENGINE = InnoDB;"
    mycursor.execute(consulta)
    
    mycursor.close()
    mydb.close()

      
def eliminaFilas():
    mydb = mysql.connector.connect(host="localhost",port=3306,user="root",database="alphaupo")
    mycursor = mydb.cursor()

    sql = "DELETE FROM `partida` WHERE YEAR(Date) < YEAR('2015-00-00')"
    
    mycursor.execute(sql)
    
    mydb.commit()
    
    mycursor.close()
    mydb.close()