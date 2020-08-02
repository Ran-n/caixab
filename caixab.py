#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	28/07/2020 21:50:39
#+ Editado:	02/08/2020 13:29:20

import codigo.modelo.manexador_sqlite as sqlite
import codigo.apis.coingeckoapi as cg
import json

def jprint (data, indentacion=4, ordear=False):
    print(json.dumps(data, indent=indentacion, sort_keys=ordear))

vBD = sqlite.cBaseDatos('persoal')
vBD.CrearBD()

vCG = cg.cCoinGecko()
valor_moedas = vCG.valor_moedas('zum-token,bitcoin,phoneum', 'eur')
#jprint(vCG.lista_moedas_referencia())
jprint(vCG.lista_moedas())
jprint(valor_moedas)


