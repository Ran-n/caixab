#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	26/08/2020 15:13:42
#+ Editado:	26/08/2020 17:03:28

from abc import ABC, abstractmethod

class InterfaceCapaModelo(ABC):
    @abstractmethod
    def valor_moedas(self, moeda_referencia):
        pass

    @abstractmethod
    def cambio_fiat(self, moeda_ini, moeda_fin):
        pass
