import string
import random as rd
import datetime as dt

numeros = list(string.digits)
alfabeto_maiusculo = list(string.ascii_uppercase)
nome = ['Pedro', 'Gabriela', 'Paulo', 'Klissia', 'Rita', 'José', 'Tiago', 'Rafael', 'Carla', 'Francisco', 'Igor', 'Fabiana', 'Fabian', 'Humberto', 'Ana', 'Bruna', 'Breno', 'Isabela']
sobrenome = ['da Silva', 'Oliveira', 'Chagas', 'Benchimol', 'dos Santos', 'Carvalho', 'Nascimento', 'Cavalcante', 'Medeiros', 'Vieira', 'Mendonca', 'Mendes']
ultimo_nome = ['Rodrigues', 'de Souza', 'Ferreira', 'Alves', 'Pereira', 'Lima', 'Gomes', 'Ribeiro', 'Guedes', 'Martins']

def gera_nome():
    nome_completo = nome[rd.randrange(0, len(nome))] + ' ' + sobrenome[rd.randrange(0, len(sobrenome))] + ' ' + ultimo_nome[rd.randrange(0, len(ultimo_nome))]
    
    return nome_completo

def gera_dataNasc():
    ano = rd.randrange(1950, 2001)
    mes = rd.randrange(1, 13)
    dia = 0
    if(mes == 2):
        dia = rd.randrange(1, 29)
    else:
        dia = rd.randrange(1, 31)
    data_nascimento = dt.date(ano, mes, dia)

    return str(data_nascimento)

def gera_passaporte():
    passaporte = alfabeto_maiusculo[rd.randrange(0, len(alfabeto_maiusculo))] + alfabeto_maiusculo[rd.randrange(0, len(alfabeto_maiusculo))]
    for i in range(6):
        passaporte += numeros[rd.randrange(0, len(numeros))]

    return passaporte

def gera_rg():
    rg = ''

    for i in range(8):
        rg += numeros[rd.randrange(0, len(numeros))]
    
    return rg

def gera_passageiro():
    passageiro = (gera_rg(), gera_nome(), gera_passaporte(), gera_dataNasc())

    return passageiro

def gera_piloto():
    piloto = (gera_nome(), gera_passaporte(), gera_dataNasc())
    
    return piloto