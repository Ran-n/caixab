#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	28/07/2020 21:50:39
#+ Editado:	05/08/2020 14:07:45

import src.modelo.manexador_sqlite as sqlite
import src.apis.coingeckoapi as cg
from threading import Thread
import json

def jprint (data, indentacion=4, ordear=False):
    print(json.dumps(data, indent=indentacion, sort_keys=ordear))

vBD = sqlite.cBaseDatos('persoal')
fioBD = Thread(target=vBD.CrearBD())
fioBD.start()


vCG = cg.cCoinGecko()
valor_moedas = vCG.valor_moedas('yusd-synthetic-token-expiring-1-september-2020,zulu-republic-token,zum-token,bitcoin,phoneum', 'eur')
    

#jprint(vCG.ping())
#jprint(vCG.lista_moedas_referencia())
#jprint([item['id'] for item in vCG.lista_moedas()])
jprint(valor_moedas)


fioBD.join()
