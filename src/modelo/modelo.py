#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	06/08/2020 10:51:24
#+ Editado:	06/08/2020 11:13:21

#* clase contexto do patrón estratexia

import src.modelo.basedatos as cbd

class CapaModelo:
    def __init__(self, bd: cbd.BaseDatos):
        # obrigamos o uso
        if isinstance(bd, cbd.BaseDatos):
            self.bd = bd
        else:
            raise ValueError("Ten que herdar de " + BaseDatos.__name__)

    def conectarBD(self):
        self.bd.conectarBD()

    def desconectarBD(self):
        self.bd.desconectarBD()

    def commit(self):
        self.bd.commit()

    def crearBD(self):
        self.bd.crearBD()

    def select(self, consulta):
        return self.bd.select(consulta)
