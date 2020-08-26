#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	05/08/2020 23:20:53
#+ Editado:	06/08/2020 15:56:32

import src.modelo.apis.coingeckoapi as cg
import src.modelo.apis.exchangeratesapi as er
# ficheiro con funcións auxiliares úteis
from src.utils import chave_dado_valor, jprint
# contexto do patrón
import src.modelo.basedatos as BD
# estratexia concreta
import src.modelo.sqlite as Sqlite

# mete na base de datos os valores das moedas
def valor_moedas(moeda_referencia):
    Select_IdDivisa_Nome_from_Divisa= "select iddivisa, nome from divisa"

    gecko = cg.CoinGecko()

    bd = BD.BaseDatos(Sqlite.Sqlite('persoal'))
    #bd.crearBD()

    fias = bd.select(Select_IdDivisa_Nome_from_Divisa)

    # se se recuperan fias
    if fias:
        moedas = ''
        for row in fias:
            moedas = moedas + ',' + row[1]

        jprint(gecko.ratio_moedas(moedas, moeda_referencia))

#
def cambio_fiat(moeda_ini, moeda_fin):
    exrate = er.ExchangeRate()

    ratio_cambio = exrate.ratio_fiat(moeda_ini.upper(), moeda_fin.upper())['rates'][moeda_fin.upper()]

    print(ratio_cambio)
