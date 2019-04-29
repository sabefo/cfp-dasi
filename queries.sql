CREATE TABLE users
(
    dni varchar(9) not null,
    name varchar(20) not null,
    PRIMARY KEY (dni)
);

CREATE TABLE Pedido(, idUsuario int , idRestaurante int, opinion varchar(200), PRIMARY KEY(idPedido), FOREIGN KEY (idRestaurante) REFERENCES Restaurante (idRestaurante) ,FOREIGN KEY (idUsuario) REFERENCES Usuario (idUsuario))


CREATE TABLE movements
(
    id int NOT NULL AUTO_INCREMENT,
    dni varchar(9) not null,
    concept varchar(20) not null,
    date datetime not null,
    amount decimal(7, 2),
    PRIMARY KEY (id),
    FOREIGN KEY (dni) REFERENCES users (dni)
);

CREATE TABLE purchases
(
    dni varchar(9) not null,
    prodcuct varchar(20) not null,
);


CREATE TABLE PedidoProducto
(
    idPedido int,
    idProducto int,
    PRIMARY KEY(idPedido, idProducto),
    FOREIGN KEY (idPedido) REFERENCES Pedido (idPedido),
    FOREIGN KEY (idProducto) REFERENCES Producto (idProducto)
)
