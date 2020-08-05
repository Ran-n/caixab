    #! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	31/07/2020 22:55:28
#+ Editado:	05/08/2020 14:17:36

import requests as r
#import coinapi

class cCoinGecko():
    def __init__(self):
        #super(cCoinGecko, self).__init__()
        self.url = 'https://api.coingecko.com/api/v3/'

    def _conexion_controlada(self, resposta):
        if resposta.ok:
            return resposta.json()
        else:
            raise ValueError('Erro de conexión')

    def ping(self):
        url_ping = self.url+'ping'

        return self._conexion_controlada(r.get(url_ping))

    def lista_moedas_referencia(self):
        url_moeda_ref = self.url+'simple/supported_vs_currencies'

        return self._conexion_controlada(r.get(url_moeda_ref))

    def lista_moedas(self):
        url_moedas = self.url+'coins/list'

        return self._conexion_controlada(r.get(url_moedas))

    def valor_moedas(self,criptos,moedas):
        url_valor_moedas = self.url+'simple/price?ids='+criptos+'&vs_currencies='+moedas

        return self._conexion_controlada(r.get(url_valor_moedas))

