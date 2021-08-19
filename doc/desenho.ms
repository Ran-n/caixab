.TL
Explicaci\*[']on sobre o desenho usado
.AU
Ran#
.AB
Explicaci\*[']on sobre diversos puntos onde se fixeron decisi\*[']ons en base a unha certa forma de ver o problema.
.AE

.SH
Diagrama Entidade Relaci\*[']on
.PSPIC -C "doc/ER_simplificado.eps" 7

.SH
Qu\*[']e se tenta representar na BD?
.PP
O obxectivo \*[']e poder almacenar na BD todos os datos precisos relativos \*[']o manexamento das finanzas.
Tanto a nivel de cartos nunha conta bancaria ou carteira (entidade "Conta"), como de metais preciosos como o outro (entidade "Conta") coa s\*[']ua correspondente divisa (euros ou gramos de ouro (gAu)).

.NH
Por qu\*[']e activo non ten relaci\*[']on total?
.PP
\*[']E menos restrictivo.
As\*[']i p\*[']odense meter activos iniciais na BD (anteriores \*[']a s\*[']ua creaci\*[']on).
Tam\*[']en permite engadir as\*[']i activos sen ter que crear unha transacci\*[']on.

.NH
Por qu\*[']e a relaci\*[']on Conta-Transacci\*[']on \*[']e 1-N e non 1..2-N?
.PP
Cada transacci\*[']on s\*[']o ten unha conta.
O s\*[']imbolo +/- indicar\*[']a se \*[']e a conta de orixe ou destino.
Desta forma, cada transacci\*[']on real corresp\*[']ondese con d\*[']uas na BD
(por exemplo: Unha transacci\*[']on de 20 euros traducir\*[']iase tal que -20 na conta 1 e +20 na conta 2.
O atributo "N\*[']umero de transacci\*[']on" permite logo poder recordar que estas d\*[']uas transacci\*[']ons da BD se corresponden cunha mesma transacci\*[']on l\*[']oxica).

.NH
Por qu\*[']e a relaci\*[']on Transacci\*[']on-Divisa \*[']e N-1 e non N-1..2?
.PP
Cada transacci\*[']on, \*[']o s\*[']o ter unha conta, s\*[']o conta cunha divisa engadida ou substraida dela.
Esta, non ten que ser a mesama que se ingresa ou substrae na segunda
(por exemplo: Conta1 -20 euros e Conta2 +5 gAu sendo ambas a mesma transacci\*[']on l\*[']oxica).
