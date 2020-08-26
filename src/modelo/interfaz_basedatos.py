#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	06/08/2020 10:39:29
#+ Editado:	06/08/2020 11:40:04

#* Interface Estratexia do patrón estratexia

from abc import ABC, abstractmethod

class BaseDatos(ABC):

    @abstractmethod
    def conectarBD(self):
        pass

    @abstractmethod
    def desconectarBD(self):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def crearBD(self):
        pass

    @abstractmethod
    def select(self, consulta):
        pass

    '''
    @abstractmethod
    def update(self, consulta):
        pass

    @abstractmethod
    def remove(self, consulta):
        pass
    '''
