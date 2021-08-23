.P1
.TL
Explicaci\[u00F3]n sobre o desenho usado
.AU
Ran#
.AB
Explicaci\[u00F3]n sobre o desenho e os diversos puntos deste onde se fixeron decisi\[u00F3]ns en base a unha certa forma de ver o problema.
.AE

.NH 1
Entidade Relaci\[u00F3]n
.SH 2
Diagrama Entidade Relaci\[u00F3]n simplificado:
.PSPIC -C "doc/BD/ER_simplificado.eps" 7

.SH 2
Que se tenta representar na BD?
.PP
O obxectivo \[u00E9] poder almacenar na BD todos os datos precisos relativos \[u00F3] manexamento das finanzas.
Tanto a nivel de cartos nunha conta bancaria ou carteira (entidade "Conta"), como de metais preciosos tal que o ouro (entidade "Conta"); coa s\[u00FA]a correspondente divisa (euros, \[u20AC] ou gramos de ouro, gAu) (entidade "Divisa").
.PP
Tam\[u00E9]n se busca gardar informaci\[u00F3]n relativa \[u00F3]s activos (entidade "Activo") e \[u00F3] seu aporte econ\[u00F3]mico (tanto o custo inicial coma o beneficio de venta no caso dun cadro ou unha acci\[u00F3]n por exemplo ou o beneficio mensual no caso dunha casa alugada).
Amais, a s\[u00FA]a relaci\[u00F3]n coa entidade "Divisa", permite manter un valor actualizado do activo e un historial das fluctuaci\[u00F3]ns no prezo.
Podendo as\[u00ED] saber en todo momento o seu valor, as\[u00ED] como a fluctuaci\[u00F3]n do prezo na inversi\[u00F3]n (mirando o que se pagou por el na primeira transacci\[u00F3]n na que aparece).
Permite tam\[u00E9]n, poder calcular todos os beneficios ou gastos relacionados co activo.
Por exemplo, de tratarse dun piso, o cobro do aluguer ter\[u00ED]a \[u00F3] activo do piso como activo na transacci\[u00F3]n.
Isto complementa \[u00E1]s etiquetas, a\[u00ED]nda que tam\[u00E9]n poder\[u00ED]an usarse para obter estes mesmos datos de usarse con esa intenci\[u00F3]n.
.PP
A entidade divisa tam\[u00E9]n ter\[u00E1] unha relaci\[u00F3]n consigo mesma onde se ir\[u00E1]n gardando as fluctaci\[u00F3]ns de valor entre as distintas divisas (1 \[u20AC] = 2 $ en tal data, etc).
.PP
Todas as transacci\[u00F3]ns e activos contar\[u00E1]n cunha serie de tags (entidade "Tag") que servir\[u00E1]n para clasificar e agrupalos.
Desta forma ser\[u00E1] moi sinxelo facer partici\[u00F3]ns e agrupamentos das transacci\[u00F3]ns l\[u00F3]xicas en forma de gr\[u00E1]ficas ou resumos de gastos e beneficios.
.PP
Tam\[u00E9]n se gardar\[u00E1] a relaci\[u00F3]n entre a divisa e os seus c\[u00E9]ntimos para saber que subdivisas ten unha divisa e cando equivale.
Por exemplo do euro os c\[u00E9]ntimos ou do bitcoin os satoshis.

.SH 2
Diagrama Entidade Relaci\[u00F3]n completo:
.PSPIC -C "doc/BD/ER.eps" 7

.SH 2
Atributos das Entidades:
.PSPIC -C "doc/BD/ER_atributos.eps" 5

.SH
D\[u00FA]bidas com\[u00FA]ns
.NH 2
Existe algunha divisa que sexa unha referencia inmutable \[u00E1] que facer referencia nas transacci\[u00F3]ns?
.PP
Si e non.
Un dos atributos da transacci\[u00F3]n ser\[u00E1] "TTSN" (Tempo de Trabalho Socialmente Necesario).
Inda que non est\[u00E9] disponhible para todas as transacci\[u00F3]ns servir\[u00E1] como baremo nas que si est\[u00E9], pois o TTSN tan s\[u00F3] cambia cunha modificaci\[u00F3]n dos m\[u00E9]todos de producci\[u00F3]n (o cal e con moita menos frecuencia ca a inflaci\[u00F3]n das moedas).
Por\[u00E9]n, non se trata dunha divisa nin ser\[u00E1] posible referencia en t\[u00F3]dolos casos.

.NH 2
Como se saber\[u00E1] o valor relativo do gastado ou ganhado nunha transacci\[u00F3]n tendo en conta a inflaci\[u00F3]n?
.PP
A entidade "Transacci\[u00F3]n" conta cun atributo chamado "TTSN" (Tempo de Trabalho Socialmente Necesario), este indica o tempo en segundos preciso para a creaci\[u00F3]n ou extracci\[u00F3]n do produto nunha transacci\[u00F3]n.
No caso de operaci\[u00F3]ns como o movemento de divisas entre contas manterase a nulo.

.NH 2
\[u00C9] posible saber relaci\[u00F3]n entre o TTSN e o valor monetario dunha Divisa?
.PP
Non estar\[u00E1] gardado explicitamente na BD, pero si ser\[u00E1] calculable atendendo \[u00F3]s valores gardados nesta.
\[u00D3] ser o "TTSN", "Divisa" e a "Data" atributos de cada transacci\[u00F3]n ser\[u00E1] posible calcular a relaci\[u00F3]n ttsn-divisa concreta.

.NH 2
Por que activo non ten relaci\[u00F3]n total?
.PP
\[u00C9] menos restrictivo.
As\[u00ED] p\[u00F3]dense meter activos iniciais na BD (anteriores \[u00E1] s\[u00FA]a creaci\[u00F3]n).
Tam\[u00E9]n permite engadir as\[u00ED] activos sen ter que crear unha transacci\[u00F3]n.

.NH 2
Por que "Transacci\[u00F3]n" non ten relaci\[u00F3]n total con "Conta"?
.PP
De tela, a BD non permitir\[u00ED]a a casu\[u00ED]stica da inclusi\[u00F3]n dun agasallo dun activo.
No caso de recibir un agasallo dun activo, a transacci\[u00F3]n tan s\[u00F3] conta cun activo; sen conta ou divisa asociadas.
De ter unha relaci\[u00F3]n total ser\[u00ED]a obrigado inclu\[u00ED]r unha conta; a cal ter\[u00ED]a que ser inventada para este caso de uso en concreto.

.NH 2
Por que "Transacci\[u00F3]n" non ten relaci\[u00F3]n total con "Divisa"?
.PP
De tela, a BD non permitir\[u00ED]a; de forma elegante, a casu\[u00ED]stica da inclusi\[u00F3]n dun agasallo dun activo.
No caso de recibir un agasallo dun activo, a transacci\[u00F3]n tan s\[u00F3] conta cun activo; sen conta ou divisa asociadas.
De ter unha relaci\[u00F3]n total ser\[u00ED]a obrigado inclu\[u00ED]r unha divisa; a cal ter\[u00ED]a que ser escollida de forma aleatoria ou seminformada de entre as existentes.

.NH 2
Por que a relaci\[u00F3]n Conta-Transacci\[u00F3]n \[u00E9] 1-N e non 1..2-N?
.PP
Cada transacci\[u00F3]n s\[u00F3] ten unha conta.
O s\[u00ED]mbolo +/- indicar\[u00E1] se \[u00E9] a conta de orixe ou destino.
Desta forma, cada transacci\[u00F3]n real corresp\[u00F3]ndese con d\[u00FA]as na BD
(por exemplo: Unha transacci\[u00F3]n de 20\[u20AC] traducir\[u00ED]ase tal que -20 na conta 1 e +20 na conta 2.
O atributo "N\[u00FA]mero de transacci\[u00F3]n" permite logo poder recordar que estas d\[u00FA]as transacci\[u00F3]ns da BD se corresponden cunha mesma transacci\[u00F3]n l\[u00F3]xica).

.NH 2
Por que "Activo" non ten relaci\[u00F3]n total con "Transacci\[u00F3]n"?
.PP
Desta forma perm\[u00ED]tese engadir activos sen ter que estar referenciados en ningunha transacci\[u00F3]n.
Isto \[u00E9] extremadamente \[u00FA]til para a hora de poblar inicialmente \[u00E1] BD.
Despois, o \[u00FA]nico caso para o que ser\[u00ED]a interesante ser\[u00ED]a o dos agasallos; pero a creaci\[u00F3]n dunha transacci\[u00F3]n sen conta e, de competer, sen divisa e valor \[u00E9] unha mellor soluci\[u00F3]n.

.NH 2
Por que a relaci\[u00F3]n Transacci\[u00F3]n-Divisa \[u00E9] N-1 e non N-1..2?
.PP
Cada transacci\[u00F3]n, \[u00F3] s\[u00F3] ter unha conta, s\[u00F3] conta cunha divisa engadida ou substraida dela.
Esta, non ten que ser a mesama que se ingresa ou substrae na segunda
(por exemplo: Conta1 -20\[u20AC] e Conta2 +5 gAu sendo ambas a mesma transacci\[u00F3]n l\[u00F3]xica).

.NH 2
Por que a relaci\[u00F3]n Activo-Divisa ten o atributo "data"?
.PP
Este atributo permite gardar un historial cos valores dun activo nunha determinada divisa.
Sen el, tan s\[u00F3] se poder\[u00ED]a acceder \[u00F3] prezo \[u00FA]ltimo de determinada divisa.

.NH 2
Por que existe a relaci\[u00F3]n Divisa-Divisa? Por qu\[u00E9] ten os atributos data e valor?
.PP
A s\[u00FA]a existencia permite establecer valores relativos entre as distintas divisas.
Por exemplo, un \[u20AC] vale tantos d\[u00F3]lares ou un bitcoin vale tantos \[u20AC] ou un gAu vale tantos bitcoins.
.PP
O atributo "data", permite manter un historial da fluctuaci\[u00F3]n destes valores na BD.
O atributo "valor", permite indicar a cantidade de divisa \[u00E1] que equivale o activo.

.NH 2
Que englobar\[u00ED]a a entidade "Conta"?
.PP
En xeral, calquer reserva de valor funxible que tenha un fluxo de aumento e diminuci\[u00F3]n corrente, constante ou reiterado.
De non telo, encaixar\[u00ED]a m\[u00E1]is como activo.
Se \[u00E9] non funxible pois xa ser\[u00ED]a un activo seguro.
.PP
Como conta modelarase calquer lugar onde se garde unha divisa.
Por exemplo: unha conta bancaria, unha carteira, un bote de moedas, etc
Tam\[u00E9]n, \[u00F3] entender unha medida do SI de material precioso como un tipo de divisa, modelaranse os materiais preciosos como por exemplo o ouro ou a prata. 

.NH 2
Que englobar\[u00ED]a a entidade "Activo"?
.PP
En xeral, calquer reserva de valor non funxible ou sen fluxo de aumento e diminuci\[u00F3]n corrente, constante ou reiterado.
.PP
Cousas como obras de arte ou casas ser\[u00ED]an os exemplos m\[u00E1]is reveladores.

.NH 2
Que englobar\[u00ED]a a entidade "Divisa"?
.PP
Calquer forma de medir o valor.
Poden ser \[u20AC], $, bitcoin ou ether pero tam\[u00E9]n gramos de ouro ou prata.

.NH 2
Como se gardar\[u00ED]an os agasallos?
.PP
Sinxelamente cunha transacci\[u00F3]n.
Se \[u00E9] un regalo de cartos, coa cantidade agasallada, a conta de destino e a divisa.
Se \[u00E9] un regalo dun activo, co elemento agasallado coa conta e divisa a nulos.

.NH 1
Modelo Relacional
.SH
Diagrama do modelo relacional
