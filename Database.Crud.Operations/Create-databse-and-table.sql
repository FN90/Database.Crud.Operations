CREATE DATABASE [Python.Crud.Operations]
GO

USE [Python.Crud.Operations]
GO

CREATE TABLE Product(Id int PRIMARY KEY IDENTITY(1,1),	Name varchar(255) NULL, Code varchar(255) NULL,	Price float NULL)