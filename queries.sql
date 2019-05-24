drop table mydb.producto;
drop table mydb.compra;
drop table mydb.movimiento;
drop table mydb.usuario;


CREATE TABLE IF NOT EXISTS `mydb`.`Usuario` (
  `Nombre` VARCHAR(45) NOT NULL,
  `Apellido_1` VARCHAR(45) NOT NULL,
  `Apellido_2` VARCHAR(45) NOT NULL,
  `DNI` VARCHAR(45) NOT NULL,
  `telegramUserID` INT NOT NULL,
  UNIQUE INDEX `DNI_UNIQUE` (`DNI` ASC) VISIBLE,
  PRIMARY KEY (`telegramUserID`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mydb`.`Compra` (
  `idCompra` INT NOT NULL AUTO_INCREMENT,
  `Concepto` VARCHAR(100) NOT NULL,
  `Monto` FLOAT NOT NULL,
  `Fecha` DATE NOT NULL,
  `Plazos` INT NULL,
  `idUsuario_FK` INT NOT NULL,
  PRIMARY KEY (`idCompra`),
  INDEX `idUser_FK_idx` (`idUsuario_FK` ASC) VISIBLE,
  CONSTRAINT `idUser_FK`
    FOREIGN KEY (`idUsuario_FK`)
    REFERENCES `mydb`.`Usuario` (`telegramUserID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mydb`.`Producto` (
  `idProducto` INT UNSIGNED NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Precio` FLOAT NOT NULL,
  `idUsuario_FK` INT NOT NULL,
  PRIMARY KEY (`idProducto`),
  INDEX `idUsuario_FK_idx` (`idUsuario_FK` ASC) VISIBLE,
  CONSTRAINT `idUsuario_FK`
    FOREIGN KEY (`idUsuario_FK`)
    REFERENCES `mydb`.`Usuario` (`telegramUserID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mydb`.`Movimiento` (
  `idMovimiento` INT NOT NULL AUTO_INCREMENT,
  `Tipo` VARCHAR(45) NOT NULL,
  `Fecha` DATE NOT NULL,
  `Monto` FLOAT NOT NULL,
  `Concepto` VARCHAR(50) NOT NULL,
  `idUsuario_FK` INT NULL,
  PRIMARY KEY (`idMovimiento`),
  INDEX `idUsuario_FK_idx` (`idUsuario_FK` ASC) VISIBLE,
  CONSTRAINT `idUsuario_FK1`
    FOREIGN KEY (`idUsuario_FK`)
    REFERENCES `mydb`.`Usuario` (`telegramUserID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



ALTER TABLE `mydb`.`Movimiento` ADD CHECK (  `Tipo` IN ('Ingreso', 'Egreso')) ;

INSERT INTO `mydb`.`Usuario` (`Nombre`, `Apellido_1`, `Apellido_2`, `DNI`, `telegramUserId`) VALUES ('Gonzalo', 'Machado', 'Salazar', 'Y7463536A', '800282905');
INSERT INTO `mydb`.`Usuario` (`Nombre`, `Apellido_1`, `Apellido_2`, `DNI`, `telegramUserId`) VALUES ('Santiago', 'Bermudez', 'Fortes', '12735395A', '851288992');


