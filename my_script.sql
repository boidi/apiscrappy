-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema my_app
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema my_app
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `my_app` DEFAULT CHARACTER SET utf8 ;
USE `my_app` ;

-- -----------------------------------------------------
-- Table `my_app`.`articles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `my_app`.`articles` (
  `sujet_id` INT NOT NULL AUTO_INCREMENT,
  `libelle` VARCHAR(255) NOT NULL,
  `url` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`sujet_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `my_app`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `my_app`.`users` (
  `idusers` INT NOT NULL AUTO_INCREMENT,
  `user_pseudo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idusers`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `my_app`.`users_comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `my_app`.`users_comments` (
  `comment_id` INT NOT NULL AUTO_INCREMENT,
  `comment_date` DATE NOT NULL,
  `contenu` VARCHAR(255) NOT NULL,
  `user_id` INT NOT NULL,
  `articles_id` INT NOT NULL,
  PRIMARY KEY (`comment_id`),
  INDEX `articles_id_idx` (`articles_id` ASC),
  CONSTRAINT `articles_id`
    FOREIGN KEY (`articles_id`)
    REFERENCES `my_app`.`articles` (`sujet_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
