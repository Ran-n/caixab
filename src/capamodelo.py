#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	05/08/2020 23:20:53
#+ Editado:	06/08/2020 11:48:52


import src.modelo.apis.coingeckoapi as cg
import src.modelo.apis.exchangeratesapi as er
from src.utils import chave_dado_valor, jprint 
# contexto do patrón
import src.modelo.basedatos as BD
# estratexia concreta
import src.modelo.sqlite as Sqlite

# mete na base de datos os valores das moedas
def valor_moedas():
    Select_IdDivisa_Nome_from_Divisa= "select iddivisa, nome from divisa"

    gecko = cg.CoinGecko()
    exrate = er.ExchangeRate()

    bd = BD.BaseDatos(Sqlite.Sqlite('persoal'))
    bd.crearBD()

    fias = bd.select(Select_IdDivisa_Nome_from_Divisa)

    # se se recuperan fias
    if fias:
        moedas = ''
        for row in fias:
            moedas = moedas + ',' + row[1]

        jprint(gecko.ratio_moedas(moedas, 'eur'))
        jprint(exrate.ratio_fiat('usd'.upper(), 'eur'.upper())['rates']['eur'.upper()])










