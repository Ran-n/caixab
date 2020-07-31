#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	28/07/2020 21:50:39
#+ Editado:	31/07/2020 23:26:07

import codigo.modelo.manexador_sqlite as sqlite
import codigo.apis.coingeckoapi as cg

vBD = sqlite.cBaseDatos('persoal')
vBD.CrearBD()

vCG = cg.cCoinGecko()
valor_moedas = vCG.valor_moedas('phoneum', 'eur')
print(valor_moedas)


