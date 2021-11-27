import sys

from gerador_aviao import gera_aviao
from gerador_aeroporto import gera_aeroporto
from gerador_pessoa import gera_passageiro, gera_piloto
from metodos_bd import *

def popula_bd(qtde_passageiros = 1000, qtde_pilotos = 50, qtde_avioes = 30, qtde_voos = 50):
    bd = conecta_bd()

    print('Iniciando inserção dos dados sintéticos...')

    for i in range(qtde_avioes):
        aviao, assentos = gera_aviao()
        insere_aviao(bd, aviao, assentos)

    insere_aeroportos(bd)

    for i in range(qtde_pilotos):
        piloto = gera_piloto()
        insere_piloto(bd, piloto)

    for i in range(qtde_passageiros):
        passageiro = gera_passageiro()
        insere_passageiro(bd, passageiro)

    for i in range(qtde_voos):
        insere_voo(bd)

    insere_passagens(bd)

    print('Inserção finalizada!')

    fecha_bd(bd)

if (len(sys.argv) == 1):
    popula_bd()

elif (len(sys.argv) == 5):
    popula_bd(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))

else:
    print('comando: python3 gerador_bd.py <qtde_passageiros> <qtde_pilotos> <qtde_avioes> <qtde_voos>')