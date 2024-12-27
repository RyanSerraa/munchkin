from Partida import *

p = Partida()

j1 = Jogador()
j1.set_nome("Jogador1")
j1.set_nivel(2)

j2 = Jogador()
j2.set_nome("Jogador2")
j2.set_nivel(9)

j3 = Jogador()
j3.set_nome("Jogador3")
j3.set_nivel(7)

p.adicionar_jogador(j1)
p.adicionar_jogador(j2)
p.adicionar_jogador(j3)

p.verificar_nivel("Jogador1")
p.verificar_nivel("Jogador2")
p.verificar_nivel("Jogador3")
p.verificar_nivel("Jogador4")
