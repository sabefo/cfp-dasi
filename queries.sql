CREATE TABLE IF NOT EXISTS `mydb`.`Usuario` (
  `idUsuario` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Apellido_1` VARCHAR(45) NOT NULL,
  `Apellido_2` VARCHAR(45) NOT NULL,
  `DNI` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idUsuario`, `DNI`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mydb`.`Compra` (
  `idCompra` INT NOT NULL AUTO_INCREMENT,
  `Concepto` VARCHAR(100) NOT NULL,
  `Monto` FLOAT NOT NULL,
  `Fecha` DATE NOT NULL,
  `Plazos` INT NULL,
  `idUsuario_FK` INT NOT NULL,
  PRIMARY KEY (`idCompra`),
  INDEX `idUsuario_FK_idx` (`idUsuario_FK` ASC) VISIBLE,
  CONSTRAINT `idUsuario_FK`
    FOREIGN KEY (`idUsuario_FK`)
    REFERENCES `mydb`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mydb`.`Producto` (
  `idProducto` INT UNSIGNED NOT NULL,
  `Cod_MercadoLibre` VARCHAR(45) NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Precio` FLOAT NOT NULL,
  `Descripcion` VARCHAR(100) NOT NULL,
  `idCompra_FK` INT NOT NULL,
  PRIMARY KEY (`idProducto`),
  INDEX `idCompra_FK_idx` (`idCompra_FK` ASC) VISIBLE,
  CONSTRAINT `idCompra_FK`
    FOREIGN KEY (`idCompra_FK`)
    REFERENCES `mydb`.`Compra` (`idCompra`)
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
  CONSTRAINT `idUsuarioM_FK`
    FOREIGN KEY (`idUsuario_FK`)
    REFERENCES `mydb`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


ALTER TABLE `mydb`.`Movimiento` ADD CHECK (  `Tipo` IN ('Ingreso', 'Egreso')) ;

INSERT INTO `mydb`.`Usuario` (`idUsuario`, `Nombre`, `Apellido_1`, `Apellido_2`, `DNI`) VALUES (1, 'Gonzalo', 'Machado', 'Salazar', 'Y7463536A');
INSERT INTO `mydb`.`Usuario` (`idUsuario`, `Nombre`, `Apellido_1`, `Apellido_2`, `DNI`) VALUES (2, 'Santiago', 'Bermudez', 'Fortes', '12735395A');

