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
        nameUser = user[1]
        query = "INSERT IGNORE INTO Usuario (idUsuario, nombreUsuario) VALUES ('{0}', '{1}');".format(user[0], user[1])
        try:
            x.execute(query)
        except MySQLdb.ProgrammingError:
            print("La siguiente query ha fallado:%s" % query + '\n')
        print("El usuario " + str(nameUser) + " ha sido añadido")
    conn.commit()
    x.close()
    conn.close()



def insertOrderProduct(orderProducts): #Le llega una lista con el id del pedido y el id del producto
    conn = connection()
    x = conn.cursor()
    query = "INSERT IGNORE INTO PedidoProducto (idPedido, idProducto) VALUES ('{0}', '{1}');".format(orderProducts[0], orderProducts[1])
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("La siguiente query ha fallado:%s" % query + '\n')
    conn.commit()
    x.close()
    conn.close()


def insertOpinion(opinion):
    conn = connection()
    x = conn.cursor()
    query = "UPDATE Pedido SET opinion = '%s' WHERE idPedido = '%i' ON DUPLICATE KEY UPDATE" % (opinion[1], opinion[0])
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("La siguiente query ha fallado:%s" % query + '\n')
    conn.commit()
    x.close()
    conn.close()


def insertOrder(orderList): #Le llega una lista con el usuario que hace el pedido y el nombre del restaurante que elije
    conn = connection()
    x = conn.cursor()
    #for order in orderList:
    idUser = orderList[0]
    nameRestaurant = orderList[1]
    idRestaurante = searchIDRestaurant(nameRestaurant)
    query = "INSERT IGNORE INTO Pedido (idUsuario, idRestaurante) VALUES ('{0}', '{1}');".format(idUser, idRestaurante)
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("La siguiente query ha fallado:%s" % query + '\n')

    print("El pedido del usuario " + str(idUser) + " para el restaurante: "+ str(nameRestaurant) +" ha sido añadido")
    conn.commit()
    x.close()
    conn.close()



def insertProducts(productsList): #Le llega una lista con los nombres de los productos
    conn = connection()
    x = conn.cursor()
    for product in productsList:
        query = "INSERT IGNORE INTO Producto (nombreProducto) VALUES ('{0}');" .format(product)
        try:
            x.execute(query)
        except MySQLdb.ProgrammingError:
            print("La siguiente query ha fallado:%s" % query + '\n')
        print("El producto " + str(product) + " ha sido añadido")
    conn.commit()
    x.close()
    conn.close()



def insertRestaurants(restaurantsList): #Le llega una lista con el nombre del restaurante y el tipo de restaurante
    conn = connection()
    x = conn.cursor()
    for restaurant in restaurantsList:
        restaurantName = restaurant[0]
        restaurantType = restaurant[1]
        query = "INSERT IGNORE INTO Restaurante (nombreRestaurante, tipoRestaurante) VALUES ('{0}', '{1}');".format(restaurant[0], restaurant[1])
        try:
            x.execute(query)
        except MySQLdb.ProgrammingError:
            print("La siguiente query ha fallado:%s" % query + '\n')
        print("El restaurante " + str(restaurant) + " ha sido añadido")
    conn.commit()
    x.close()
    conn.close()



def insertRestaurantProducts(restaurantProductList): #Le llega una lista con el id del restaurante y el id del producto
    conn = connection()
    x = conn.cursor()
    for productRestaurant in restaurantProductList:
        idRestaurant = productRestaurant[0]
        idProduct = productRestaurant[1]
        query = "INSERT IGNORE INTO RestauranteProducto (idRestaurante, idProducto) VALUES ('{0}', '{1}');".format(
            idRestaurant, idProduct)
        try:
            x.execute(query)
        except MySQLdb.ProgrammingError:
            print("La siguiente query ha fallado:%s" % query + '\n')
        print("El restaurante " + str(productRestaurant) + " ha sido añadido")
    conn.commit()
    x.close()
    conn.close()



def deleteDatabase():
    conn = connection()
    x = conn.cursor()
    query = "DROP TABLE IF EXISTS PedidoProducto;" # IF EXISTS(SELECT * FROM  dbo.Producto) DROP TABLE Producto; IF EXISTS(SELECT * FROM  dbo.Restaurante) DROP TABLE Restaurante;"
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("Fallo:%s" % query + '\n')
    conn.commit()
    query = "DROP TABLE IF EXISTS Pedido;"  # IF EXISTS(SELECT * FROM  dbo.Producto) DROP TABLE Producto; IF EXISTS(SELECT * FROM  dbo.Restaurante) DROP TABLE Restaurante;"
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("Fallo:%s" % query + '\n')
    conn.commit()
    query = "DROP TABLE IF EXISTS Usuario;"  # IF EXISTS(SELECT * FROM  dbo.Producto) DROP TABLE Producto; IF EXISTS(SELECT * FROM  dbo.Restaurante) DROP TABLE Restaurante;"
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("Fallo:%s" % query + '\n')
    conn.commit()
    query = "DROP TABLE IF EXISTS PedidoProducto;"  # IF EXISTS(SELECT * FROM  dbo.Producto) DROP TABLE Producto; IF EXISTS(SELECT * FROM  dbo.Restaurante) DROP TABLE Restaurante;"
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("Fallo:%s" % query + '\n')
    conn.commit()
    query = "DROP TABLE IF EXISTS RestauranteProducto;"  # IF EXISTS(SELECT * FROM  dbo.Producto) DROP TABLE Producto; IF EXISTS(SELECT * FROM  dbo.Restaurante) DROP TABLE Restaurante;"
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("Fallo:%s" % query + '\n')
    conn.commit()
    query = "DROP TABLE IF EXISTS Producto;"  # IF EXISTS(SELECT * FROM  dbo.Producto) DROP TABLE Producto; IF EXISTS(SELECT * FROM  dbo.Restaurante) DROP TABLE Restaurante;"
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("Fallo:%s" % query + '\n')
    conn.commit()
    query = "DROP TABLE IF EXISTS Restaurante;"  # IF EXISTS(SELECT * FROM  dbo.Producto) DROP TABLE Producto; IF EXISTS(SELECT * FROM  dbo.Restaurante) DROP TABLE Restaurante;"
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("Fallo:%s" % query + '\n')
    print("Tablas borradas")
    conn.commit()
    x.close()
    conn.close()



def createTables():
    conn = connection()
    x = conn.cursor()
    query = "CREATE TABLE Producto(idProducto int NOT NULL AUTO_INCREMENT,nombreProducto varchar(100), UNIQUE(nombreProducto),PRIMARY KEY (idProducto)) ; "
    try:
        x.execute(query)
    except MySQLdb.Warning:
        print("Fallo:%s" % query + '\n')
    conn.commit()
    query = "CREATE TABLE Restaurante(idRestaurante int NOT NULL AUTO_INCREMENT,nombreRestaurante varchar(100), tipoRestaurante varchar(100), PRIMARY KEY (idRestaurante),UNIQUE(nombreRestaurante)) ; "
    try:
        x.execute(query)
    except MySQLdb.Warning:
        print("Fallo:%s" % query + '\n')
    conn.commit()
    query = "CREATE TABLE RestauranteProducto(idRestaurante int, idProducto int, PRIMARY KEY (idRestaurante, idProducto),FOREIGN KEY (idRestaurante) REFERENCES Restaurante (idRestaurante),FOREIGN KEY (idProducto) REFERENCES Producto (idProducto)) ;"
    try:
        x.execute(query)
    except MySQLdb.Warning:
        print("Fallo:%s" % query + '\n')
    print("Tablas creadas")
    conn.commit()
    query = "CREATE TABLE Usuario( idUsuario int, nombreUsuario varchar(100), PRIMARY KEY(idUsuario));"

    try:
        x.execute(query)
    except MySQLdb.Warning:
        print("Fallo:%s" % query + '\n')
    print("Tablas creadas")

    conn.commit()
    query = "CREATE TABLE Pedido(idPedido int NOT NULL AUTO_INCREMENT, idUsuario int , idRestaurante int, opinion varchar(200), PRIMARY KEY(idPedido), FOREIGN KEY (idRestaurante) REFERENCES Restaurante (idRestaurante) ,FOREIGN KEY (idUsuario) REFERENCES Usuario (idUsuario))";
    try:
        x.execute(query)
    except MySQLdb.Warning:
        print("Fallo:%s" % query + '\n')
    print("Tablas creadas")
    conn.commit()
    query = "CREATE TABLE PedidoProducto( idPedido int, idProducto int, PRIMARY KEY(idPedido, idProducto), FOREIGN KEY (idPedido) REFERENCES Pedido (idPedido), FOREIGN KEY (idProducto) REFERENCES Producto (idProducto))";
    try:
        x.execute(query)
    except MySQLdb.Warning:
        print("Fallo:%s" % query + '\n')
    print("Tablas creadas")
    conn.commit()
    x.close()
    conn.close()



def searchFoodType(): #Devuelve la lista de los tipos de restaurantes
    conn = connection()
    x = conn.cursor()
    typeRestaurantList = []
    query = "SELECT DISTINCT tipoRestaurante FROM Restaurante ;".format(str)
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("La siguiente query ha fallado: " + query + '\n')
    for line in x:
        typeRestaurantList.append(line[0])
    conn.commit()
    x.close()
    conn.close()
    return typeRestaurantList



def searchRestaurantType(restaurantType): #Devuelve una lista de los restaurantes de un tipo
    conn = connection()
    x = conn.cursor()
    listaRestaurantes = []
    escaped = re.escape(restaurantType)
    query = "SELECT DISTINCT nombreRestaurante FROM Restaurante WHERE tipoRestaurante LIKE '%s' " %("%" + restaurantType + "%")
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("La siguiente query ha fallado: " + query + '\n')
    for line in x:
        listaRestaurantes.append(line[0])
    conn.commit()
    x.close()
    conn.close()
    return listaRestaurantes


def searchRestaurant(): #Devuelve una lista de los restaurantes
    conn = connection()
    x = conn.cursor()
    listaRestaurantes = []

    query = "SELECT DISTINCT nombreRestaurante FROM Restaurante;"
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("La siguiente query ha fallado: " + query + '\n')
    for line in x:
        listaRestaurantes.append(line[0])
    conn.commit()
    x.close()
    conn.close()
    return listaRestaurantes


def searchIDRestaurant(restaurantName): #Devuelve el id del restaurante introducido
    conn = connection()
    x = conn.cursor()
    query = "SELECT DISTINCT idRestaurante FROM Restaurante WHERE nombreRestaurante LIKE '%s' " %("%" + restaurantName + "%")
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("La siguiente query ha fallado: " + query + '\n')
    idRestaurant = x.fetchall()
    idRestaurant = idRestaurant[0][0]
    conn.commit()
    x.close()
    conn.close()
    return idRestaurant


def searchIDProduct(productName): #Devuelve el id del restaurante introducido
    conn = connection()
    x = conn.cursor()
    query = "SELECT DISTINCT idProducto FROM Producto WHERE nombreProducto LIKE '%s' " %("%" + productName + "%")
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("La siguiente query ha fallado: " + query + '\n')
    idProduct = x.fetchall()
    idProduct = idProduct[0][0]
    conn.commit()
    x.close()
    conn.close()
    return idProduct


def searchProductsFromRestaurant(restaurantName): #Busca los productos de un restaurante
    conn = connection()
    x = conn.cursor()
    productsList = []
    escaped = re.escape(restaurantName)
    query = "SELECT DISTINCT nombreProducto FROM Producto NATURAL JOIN RestauranteProducto NATURAL JOIN" \
            " Restaurante WHERE nombreRestaurante LIKE '%s' " %("%" + restaurantName + "%")
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("La siguiente query ha fallado: " + query + '\n')
    for line in x:
        productsList.append(line[0])
    conn.commit()
    x.close()
    conn.close()
    return productsList


def searchOpinionFromRestaurant(restaurantId): #Busca los productos de un restaurante
    conn = connection()
    x = conn.cursor()
    query = "SELECT opinion FROM Pedido WHERE idRestaurante = '%i' ORDER BY idPedido DESC LIMIT 1;" % (restaurantId)
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("La siguiente query ha fallado: " + query + '\n')
    opinion = x.fetchall()
    if len(opinion) > 0:
        opinion = opinion[0][0]
    conn.commit()
    x.close()
    conn.close()
    return opinion


def searchOrder(idUser, restaurantName): #Devuelve el id del ultimo pedido que se ha insertado
    conn = connection()
    x = conn.cursor()
    idRestaurant = searchIDRestaurant(restaurantName)
    query = "SELECT idPedido FROM Pedido WHERE idUsuario = '%s'  AND idRestaurante = '%s' AND idPedido = (SELECT max(idPedido) FROM Pedido)" % (idUser, idRestaurant)
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("La siguiente query ha fallado: " + query + '\n')
    idProduct = x.fetchall()
    for line in x:
        idOrder = line[0]
    conn.commit()
    x.close()
    conn.close()
    return idOrder



def searchOrderForUser(idUser): #Devuelve el id del ultimo restaurante en el que ha pedido el usuario

    conn = connection()
    x = conn.cursor()
    query = "SELECT idRestaurante FROM Pedido WHERE idUsuario = '%i' ORDER BY idPedido DESC LIMIT 1;" % (idUser)
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("La siguiente query ha fallado: " + query + '\n')
    idRestaurant = x.fetchall()
    idRestaurant = idRestaurant[0][0]
    conn.commit()
    x.close()
    conn.close()
    return idRestaurant


def searchRestaurantForOrder(idRestaurant): #Devuelve el tipo de restaurante de ese idRestaurante
    conn = connection()
    x = conn.cursor()
    query = "SELECT tipoRestaurante FROM Restaurante WHERE idRestaurante = '%i';" % (idRestaurant)
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("La siguiente query ha fallado: " + query + '\n')
    restaurantType = x.fetchall()
    restaurantType = restaurantType[0][0]
    conn.commit()
    x.close()
    conn.close()
    return restaurantType


def searchRestaurantTypeSimilar(restaurantType, idRestaurant): #Devuelve los restaurantes de ese tipo

    conn = connection()
    x = conn.cursor()
    restaurantName = []

    query = "SELECT nombreRestaurante FROM Restaurante WHERE tipoRestaurante = '%s' AND idRestaurante <> '%i';" % (restaurantType, idRestaurant)
    try:
        x.execute(query)
    except MySQLdb.ProgrammingError:
        print("La siguiente query ha fallado: " + query + '\n')


    for line in x:
        restaurantName.append(line[0])
    conn.commit()
    x.close()
    conn.close()
    restaurant = random.choice(restaurantName)
    return restaurant
