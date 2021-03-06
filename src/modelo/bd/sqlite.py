#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	27/07/2020 08:48:52
#+ Editado:	26/08/2020 17:27:17

#* Clase estratexia concreta do patrón estratexia

import sqlite3
from sqlite3 import Error
import os

import src.modelo.bd.interfaz_basedatos as bd
# ficheiro py cos catexs de creación das táboas
import src.modelo.bd.taboas_sqlite as taboa

class Sqlite(bd.BaseDatos):
    def __init__(self, ficheiro_bd):
        '''
            ficheiro_bd > Catex
        '''

        self.ficheiro_bd = './media/' + ficheiro_bd + '.bd'
        self.conn = sqlite3.connect(self.ficheiro_bd)
        self.taboas = [taboa.Conta, taboa.Divisa, taboa.ValorRelativoDivisa, taboa.Etiqueta, taboa.Transaccion, taboa.EtiquetadoTransaccion]

    def _collerCursor(self):
        return self.conn.cursor()

    # función para conectarse á base de datos
    def conectarBD(self):
        self.conn = sqlite3.connect(self.ficheiro_bd)

    # función para desconectarse da base de datos
    def desconectarBD(self):
        self.conn.close()

    # commit dos cambios
    def commit(self):
        self.conn.commit()

    # Crea o ficheiro e as táboas do mesmo se non existe xa
    def crearBD(self):
        cursor = self._collerCursor()
        # select de tódalas táboas do ficheiro
        cursor.execute('''select name from sqlite_master where type='table';''')

        # lista das táboas da BD

        # se non ten tódalas táboas algo anda mal
        if len(cursor.fetchall()) != len(self.taboas):
            try:
                # eliminamos o ficheiro
                os.remove(self.ficheiro_bd)
                # conectamonos á base de datos de novo
                self.conectarBD()
                # creamos tódalas táboas
                self._crearTaboa(self.taboas)

            except Error as e:
                print(e)

    # crea unha ou varias databoas dada unha lista cos creates en catex
    def _crearTaboa(self, taboas):
        '''
            taboas  > Lista de catexs coas sentenzas de creación
        '''

        # collemos o cursor
        cursor = self._collerCursor()

        # facemos o execute dos create table
        for taboa in taboas:
            cursor.execute(taboa)

        self.commit()

    # Executa unha consulta e devolve as fias do resultado
    def select(self, consulta):
        '''
            consulta > Catex coa sentenza select
        '''

        # collemos o cursor
        cursor = self._collerCursor()
        # executamos a consulta
        cursor.execute(consulta)

        return cursor.fetchall()
