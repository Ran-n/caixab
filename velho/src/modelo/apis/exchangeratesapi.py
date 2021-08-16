#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	05/08/2020 19:34:13
#+ Editado:	06/08/2020 13:06:51

import requests as r

class ExchangeRate:
    def __init__(self):
        self.url = 'https://api.exchangeratesapi.io/'

    def _conexion_controlada(self, resposta):
        if resposta.ok:
            return resposta.json()
        else:
            raise ValueError('Erro de conexión')

    def ratio_fiat(self,moeda_de,moeda_a):
        url = self.url + 'latest?base='+ moeda_de +'&symbols=' + moeda_a
        
        return self._conexion_controlada(r.get(url))
