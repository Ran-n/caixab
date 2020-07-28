#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	28/07/2020 21:50:39
#+ Editado:	28/07/2020 21:50:39

import codigo.modelo.manexador_sqlite as sqlite

vBD = sqlite.cBaseDatos('persoal')
vBD.CrearBD()
