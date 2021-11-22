import string
import random as rd

alfabeto_maiusculo = list(string.ascii_uppercase)
numeros = list(string.digits)
nomes_aviao = ['Airbus', 'Boeing', 'Bombardier', 'Cessna', 'Embraer', 'Tupolev']

def gera_assentos(num_serie_aviao):
    assentos = []
    qtde_assentos = rd.randrange(100, 351)

    for i in range(qtde_assentos):
        tipo = ''
        if(rd.randrange(0, 100) >= 80):
            tipo = 'EX'

        else:
            tipo = 'EC'

        assento = (tipo, num_serie_aviao)
        assentos.append(assento)

    return assentos

def gera_aviao():
    modelo = nomes_aviao[rd.randrange(0, len(nomes_aviao))] + ' '
    num_serie = alfabeto_maiusculo[rd.randrange(0, len(alfabeto_maiusculo))] + alfabeto_maiusculo[rd.randrange(0, len(alfabeto_maiusculo))]

    for i in range(5):
        num_serie += numeros[rd.randrange(0, len(numeros))]

    for i in range(3):
        modelo += numeros[rd.randrange(0, len(numeros))]

    aviao = (num_serie, modelo)
    assentos = gera_assentos(num_serie)

    return aviao, assentos