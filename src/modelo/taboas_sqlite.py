#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	05/08/2020 22:07:24
#+ Editado:	06/08/2020 11:47:20

#* Strings de creación das táboas sqlite

# Táboa Conta
Conta = """
CREATE TABLE "Conta" (
    "IdConta"           TEXT UNIQUE,
    "Nome"              TEXT,
    "Instante Creacion" INTEGER,
    "Descripcion"       TEXT,         
CONSTRAINT contaPK PRIMARY KEY ("IdConta")
);
"""

# Táboa Divisa
Divisa = """
CREATE TABLE "Divisa" (
    "IdDivisa"                  TEXT UNIQUE,
    "Nome"                      TEXT,
    "Simbolo"                   TEXT,
    "Siglas"                    TEXT,
    "Instante Insercion"        INTEGER,
    "Data Inicio Circulacion"   INTEGER,
    "Tipo"                      String,        
CONSTRAINT divisaPK PRIMARY KEY ("IdDivisa")
);
"""

# Táboa ValorRelativoDivisa
ValorRelativoDivisa = """ 
CREATE TABLE "ValorRelativoDivisa" (
    "IdDivisaAComparar"     TEXT,
    "IdDivisaReferencia"    TEXT,
    "Instante"              INTEGER,
    "ValorUnidade"          FLOAT,
CONSTRAINT vrdPK PRIMARY KEY ("IdDivisaAComparar", "IdDivisaReferencia"),
CONSTRAINT vrdFK1 FOREIGN KEY ("IdDivisaAComparar") REFERENCES "Divisa" ("IdDivisa"),
CONSTRAINT vrdFK2 FOREIGN KEY ("IdDivisaReferencia") REFERENCES "Divisa" ("IdDivisa")
);
"""

# Táboa Etiqueta
Etiqueta = """
CREATE TABLE "Etiqueta" (
    "IdEtiqueta"        TEXT UNIQUE,
    "Nome"              TEXT,
    "Descripcion"       TEXT,
    "Instante Creacion" TEXT,
CONSTRAINT etiquetaPK PRIMARY KEY ("IdEtiqueta")
);
"""

# Táboa Transaccion
Transaccion = """
CREATE TABLE "Transaccion" (
    "IdTransaccion" TEXT UNIQUE,
    "Instante"      INTEGER,
    "Cantidade"     TEXT,
    "IdDivisa"      TEXT,
    "IdConta"       TEXT,
    "Nome"          TEXT,
    "Notas"         TEXT,
CONSTRAINT transaccionPK  PRIMARY KEY ("IdTransaccion"),
CONSTRAINT transaccionFK1 FOREIGN KEY ("IdDivisa")  REFERENCES "Divisa" ("IdDivisa"),
CONSTRAINT transacciónFK2 FOREIGN KEY ("IdConta")   REFERENCES "Conta" ("IdConta")
);
"""

# Táboa EtiquetadoTransaccion
EtiquetadoTransaccion = """
CREATE TABLE "EtiquetadoTransaccion" (
    "IdEtiqueta"    TEXT,
    "IdTransaccion" TEXT,
CONSTRAINT etPK PRIMARY KEY ("IdEtiqueta", "IdTransaccion"),
CONSTRAINT etFK1 FOREIGN KEY ("IdEtiqueta") REFERENCES "Etiqueta" ("IdEtiqueta"),
CONSTRAINT etFK2 FOREIGN KEY ("IdTransaccion") REFERENCES "Transaccion" ("IdTransaccion")
);
"""
