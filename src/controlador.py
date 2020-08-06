#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	05/08/2020 23:20:53
#+ Editado:	06/08/2020 11:48:52


import src.modelo.apis.coingeckoapi as cg
from src.utils import chave_dado_valor, jprint 
# contexto do patrón
import src.modelo.modelo as cm
# estratexia concreta
import src.modelo.sqlite as sqlite

# mete na base de datos os valores das moedas
def valor_moedas():
    Select_IdDivisa_Nome_from_Divisa= "select iddivisa, nome from divisa"

    gecko = cg.cCoinGecko()

    bd = cm.CapaModelo(sqlite.Sqlite('persoal'))
    bd.crearBD()

    fias = bd.select(Select_IdDivisa_Nome_from_Divisa)

    # se se recuperan fias
    if fias:
        moedas = ''
        for row in fias:
            moedas = moedas + ',' + row[1]

        jprint(gecko.ratio_moedas(moedas, 'eur'))
        jprint(gecko.ratio_moedas('usd', 'eur'))










