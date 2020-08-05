#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	05/08/2020 19:03:21
#+ Editado:	05/08/2020 19:18:05

import json

def chave_dado_valor(diccionario, valor):
    return list(diccionario.keys())[list(diccionario.values()).index(valor)]

def jprint(data, indentacion=4, ordear=False):
    print(json.dumps(data, indent=indentacion, sort_keys=ordear))
