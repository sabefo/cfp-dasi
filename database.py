# coding=utf-8
# http://mysql-python.sourceforge.net/MySQLdb.html
import MySQLdb
import time


# Método para conectarse a la base de datos
def connection():
    conn = MySQLdb.connect(host= "localhost",
                           user="root",
                           passwd="root",
                           db="mydb")
    return conn

# Método para insertar un usuario en la base de datos
def insertUser(listUser):
    conn = connection()
    x = conn.cursor()
    for user in listUser:
        idUser = user[0]
        first_name = user[1]
        last_name = user[2]
        query = "INSERT IGNORE INTO Usuario (Nombre, apellido_1, telegramUserId) VALUES ('{0}','{1}','{2}');".format(first_name, last_name, idUser)
        try:
            x.execute(query)
        except MySQLdb.ProgrammingError:
            print("La siguiente query ha fallado:%s" % query + '\n')
        print("El usuario " + str(first_name) + ' ' + str(last_name) + " ha sido añadido")
    conn.commit()
    x.close()
    conn.close()

# Método para regresar la información del balance de cuenta del usuario.
def getOverallBalance(chat_id):
    balanceInfo = {}
    conn = connection()
    x = conn.cursor()
    query ="SELECT sum(CASE Tipo WHEN 'Ingreso' THEN (monto) WHEN 'Egreso' THEN -(monto) END) AS overall_balance, (select count(tipo) FROM mydb.usuario usuario, mydb.movimiento movimiento where telegramUserID={0} and usuario.telegramUserID=movimiento.idUsuario_FK and tipo='Ingreso') as ingreso, (select count(tipo) FROM mydb.usuario usuario, mydb.movimiento movimiento where telegramUserID={0} and usuario.telegramUserID=movimiento.idUsuario_FK and tipo='Egreso') as egreso  FROM mydb.usuario usuario, mydb.movimiento movimiento where telegramUserID={0} and usuario.telegramUserID=movimiento.idUsuario_FK".format(chat_id)
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

# Método para insertar una transacción de ingreso o egreso a la base de datos
def insertTransaction(chat_id, transactionType, amount, concept):
    conn = connection()
    x = conn.cursor()
    query = "INSERT IGNORE INTO Movimiento (Tipo, Fecha, Monto, Concepto, idUsuario_FK) VALUES ('{0}','{1}','{2}','{3}', '{4}');".format(transactionType, time.strftime("%Y/%m/%d"), int(amount), concept, chat_id)
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("La siguiente query ha fallado:%s" % query + '\n')
    conn.commit()
    x.close()
    conn.close()

# Método para insertar un producto en la base de datos
def insertProduct(chat_id, name, price):
    conn = connection()
    x = conn.cursor()
    query = "INSERT IGNORE INTO Producto (idUsuario_FK, Nombre, Precio) VALUES ('{0}','{1}','{2}');".format(chat_id, name[:44], price)
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("La siguiente query ha fallado:%s" % query + '\n')
    conn.commit()
    x.close()
    conn.close()
