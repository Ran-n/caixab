#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	06/08/2020 10:51:24
#+ Editado:	26/08/2020 17:27:27

#* clase contexto do patrón estratexia

import src.modelo.bd.interfaz_basedatos as ibd

class BaseDatos:
    def __init__(self, bd: ibd.BaseDatos):
        # obrigamos o uso dunha instancia
        if isinstance(bd, ibd.BaseDatos):
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

    '''
    def update(self, consulta):
        return self.bd.update(consulta)

    def remove(self, consulta):
        return self.bd.remove(consulta)
    '''
