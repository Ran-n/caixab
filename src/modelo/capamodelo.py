#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	05/08/2020 23:20:53
#+ Editado:	26/08/2020 17:28:23

# apis de criptomoedas e cambio entre fiats
import src.modelo.apis.coingeckoapi as cg
import src.modelo.apis.exchangeratesapi as er
# ficheiro con funcións auxiliares úteis
from src.utils import chave_dado_valor, jprint
# interface da capamodelo
import src.modelo.InterfaceCapamodelo as icm
# contexto do patrón
import src.modelo.bd.basedatos as BD
# estratexia concreta
import src.modelo.bd.sqlite as Sqlite

class CapaModelo(icm.InterfaceCapaModelo):
    # mete na base de datos os valores das moedas
    def valor_moedas(self, moeda_referencia):
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
    def cambio_fiat(self, moeda_ini, moeda_fin):
        exrate = er.ExchangeRate()

        ratio_cambio = exrate.ratio_fiat(moeda_ini.upper(), moeda_fin.upper())['rates'][moeda_fin.upper()]

        print(ratio_cambio)
