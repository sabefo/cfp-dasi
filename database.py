# coding=utf-8
# http://mysql-python.sourceforge.net/MySQLdb.html
import MySQLdb

# http://docs.python-requests.org/en/master/
import requests

# https://docs.python.org/2/library/re.html
import re

# https://docs.python.org/2/library/random.html
import random

def connection():
    conn = MySQLdb.connect(host= "localhost",
                           user="root",
                           passwd="root",
                           db="mydb")
    return conn



def insertUser(listUser): #Le llega una lista con el id del usuario y el nombre del usuario
    conn = connection()
    x = conn.cursor()
    for user in listUser:
        idUser = user[0]
        first_name = user[1]
        last_name = user[2]
        query = "INSERT IGNORE INTO Usuario (Nombre, apellido_1,telegramUserId) VALUES ('{0}','{1}','{2}');".format(first_name, last_name, idUser)
        try:
            x.execute(query)
        except MySQLdb.ProgrammingError:
            print("La siguiente query ha fallado:%s" % query + '\n')
        print("El usuario " + str(first_name)+ ' ' + str(last_name) + " ha sido añadido")
    conn.commit()
    x.close()
    conn.close()


def getOverallBalance(chat_id):
    balanceInfo = {}
    conn = connection()
    x = conn.cursor()
    query ="SELECT sum(CASE Tipo WHEN 'Ingreso' THEN (monto) WHEN 'Egreso' THEN -(monto) END) AS overall_balance, ( select count(tipo) as Ingreso from mydb.movimiento where tipo = 'Ingreso') as Ingreso, (select count(tipo) as Ingreso from mydb.movimiento where tipo = 'Egreso') as Egreso FROM mydb.usuario usuario, mydb.movimiento movimiento where usuario.idUsuario=movimiento.idUsuario_FK and telegramUserID={0}".format(chat_id)
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print ("No se ha podido calcular su balance general")
    queryResult = x.fetchall()
    balanceInfo["overall"] = queryResult[0][0]
    balanceInfo["ingresos"] = queryResult[0][1]
    balanceInfo["egresos"] = queryResult[0][2]
    conn.commit()
    x.close()
    conn.close()
    return balanceInfo

    
def insertTransaction(listUser): #Le llega una lista con el id del usuario y el nombre del usuario
    conn = connection()
    x = conn.cursor()
    for user in listUser:
        idUser = user[0]
        first_name = user[1]
        last_name = user[2]
        query = "INSERT IGNORE INTO Usuario (Nombre, apellido_1,telegramUserId) VALUES ('{0}','{1}','{2}');".format(first_name, last_name, idUser)
        try:
            x.execute(query)
        except MySQLdb.ProgrammingError:
            print("La siguiente query ha fallado:%s" % query + '\n')
        print("El usuario " + str(first_name)+ ' ' + str(last_name) + " ha sido añadido")
    conn.commit()
    x.close()
    conn.close()
