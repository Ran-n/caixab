#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	27/07/2020 08:48:52
#+ Editado:	28/07/2020 21:07:36

import sqlite3
from sqlite3 import Error

class cBaseDatos:
    def __init__(self, ficheiro_bd):
        self.ficheiro_bd = './media/'+ficheiro_bd+'.bd'

    # creamos a BD e as súas táboas
    def CrearBD(self):
        conn = None

        try:
            # establecemos conexión coa DB
            self.conn = sqlite3.connect(self.ficheiro_bd)
            # chamamos á función de creación das táboas
            self._CrearTaboas()
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    # función interna de creación das táboas
    def _CrearTaboas(self):
        taboa_conta = """ CREATE TABLE "Conta" (
                            "IdConta"           TEXT UNIQUE,
                            "Nome"              TEXT,
                            "Instante Creacion" INTEGER,
                            "Descripcion"       TEXT,
                            CONSTRAINT contaPK PRIMARY KEY ("IdConta")
                        ); """
                    
        taboa_divisa = """ CREATE TABLE "Divisa" (
                            "IdDivisa"                  TEXT UNIQUE,
                            "Nome"                      TEXT,
                            "Simbolo"                   TEXT,
                            "Siglas"                    TEXT,
                            "Instante Insercion"        INTEGER,
                            "Data Inicio Circulacion"   INTEGER,
                            "Tipo"                      String,
                            CONSTRAINT divisaPK PRIMARY KEY ("IdDivisa")
                        ); """
                    
        taboa_vrd = """ CREATE TABLE "ValorRelativoDivisa" (
                            "IdDivisaAComparar"     TEXT,
                            "IdDivisaReferencia"    TEXT,
                            "Instante"              INTEGER,
                            "ValorUnidade"          FLOAT,
                            CONSTRAINT vrdPK PRIMARY KEY ("IdDivisaAComparar", "IdDivisaReferencia"),
                            CONSTRAINT vrdFK1 FOREIGN KEY ("IdDivisaAComparar") REFERENCES "Divisa" ("IdDivisa"),
                            CONSTRAINT vrdFK2 FOREIGN KEY ("IdDivisaReferencia") REFERENCES "Divisa" ("IdDivisa")
                        ); """
        taboa_etiqueta = """ CREATE TABLE "Etiqueta" (
                                "IdEtiqueta"        TEXT UNIQUE,
                                "Nome"              TEXT,
                                "Descripcion"       TEXT,
                                "Instante Creacion" TEXT,
                                CONSTRAINT etiquetaPK PRIMARY KEY ("IdEtiqueta")
                            ); """
                    
        taboa_transaccion = """ CREATE TABLE "Transaccion" (
                                    "IdTransaccion" TEXT UNIQUE,
                                    "Instante"      INTEGER,
                                    "Cantidade"     TEXT,
                                    "IdDivisa"      TEXT,
                                    "IdConta"       TEXT,
                                    "Nome"          TEXT,
                                    "Notas"         TEXT,
                                    CONSTRAINT transaccionPK PRIMARY KEY ("IdTransaccion"),
                                    CONSTRAINT transaccionFK1 FOREIGN KEY ("IdDivisa") REFERENCES "Divisa" ("IdDivisa"),
                                    CONSTRAINT transacciónFK2 FOREIGN KEY ("IdConta") REFERENCES "Conta" ("IdConta")
                                ); """
                    
        taboa_et = """ CREATE TABLE "EtiquetadoTransaccion" (
                            "IdEtiqueta"    TEXT,
                            "IdTransaccion" TEXT,
                            CONSTRAINT etPK PRIMARY KEY ("IdEtiqueta", "IdTransaccion"),
                            CONSTRAINT etFK1 FOREIGN KEY ("IdEtiqueta") REFERENCES "Etiqueta" ("IdEtiqueta"),
                            CONSTRAINT etFK2 FOREIGN KEY ("IdTransaccion") REFERENCES "Transaccion" ("IdTransaccion")
                        ); """

        # collemos o cursor
        cursor = self.conn.cursor()

        # facemos os execute dos create table
        cursor.execute(taboa_conta)
        cursor.execute(taboa_divisa)
        cursor.execute(taboa_vrd)
        cursor.execute(taboa_etiqueta)
        cursor.execute(taboa_transaccion)
        cursor.execute(taboa_et)

        # ao rematar facemos commit, funciona sen poñelo
        self.conn.commit()
        

vBD = cBaseDatos('proba')
vBD.CrearBD()
