#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	28/07/2020 21:50:39
#+ Editado:	26/08/2020 17:23:03

from threading import Thread

import src.modelo.capamodelo as cm

modelo = cm.CapaModelo()

modelo.valor_moedas('eur')
modelo.cambio_fiat('eur','usd')

#vBD.crearTaboa([taboa.Conta, taboa.Divisa, taboa.ValorRelativoDivisa, taboa.Etiqueta, taboa.Transaccion, taboa.EtiquetadoTransaccion])
#fioBD = Thread(target=vBD.CrearBD())
#fioBD.start()
#vBD.valor_moedas()


#vCG = cg.cCoinGecko()
#valor_moedas = vCG.valor_moedas('yusd-synthetic-token-expiring-1-september-2020,zulu-republic-token,zum-token,bitcoin,phoneum', 'eur')


#jprint(vCG.ping())
#jprint(vCG.lista_moedas_referencia())
#jprint([item['id'] for item in vCG.lista_moedas()])
#jprint(ratio_moedas)


#fioBD.join()
