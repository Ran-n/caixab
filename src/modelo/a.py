#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	05/08/2020 23:20:53
#+ Editado:	05/08/2020 23:46:24


import src.modelo.apis.coingeckoapi as cg
from src.utils import chave_dado_valor, jprint 
import src.modelo.sqlite as sqlite

# mete na base de datos os valores das moedas
def valor_moedas():
    Select_IdDivisa_Nome_from_Divisa= "select iddivisa, nome from divisa"

    vCG = cg.cCoinGecko()

    vBD = sqlite.BaseDatos('persoal')
    vBD.crearBD()

    fias = vBD.select(Select_IdDivisa_Nome_from_Divisa)

    # se se recuperan fias
    if fias:
        moedas = ''
        for row in fias:
            moedas = moedas + ',' + row[1]

        jprint(vCG.ratio_moedas(moedas, 'eur'))
        jprint(vCG.ratio_moedas('usd', 'eur'))










