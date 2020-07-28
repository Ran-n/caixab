#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	27/07/2020 08:48:52
#+ Editado:	27/07/2020 09:18:15

import sqlite3
from sqlite3 import Error

class cBaseDatos:
    def __init__(self, ficheiro_bd):
        self.ficheiro_bd = './media/'+ficheiro_bd+'.bd'

    def CrearBD(self):
        conn = None
        try:
            conn = sqlite3.connect(self.ficheiro_bd)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()



vBD = cBaseDatos('proba')
vBD.CrearBD()

