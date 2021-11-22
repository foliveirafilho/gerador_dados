import mysql.connector
import random as rd
import datetime as dt
from mysql.connector import errorcode

def conecta_bd(host='localhost', user='root', password='root', database='companhia_aerea'):
    bd = mysql.connector.connect(host=host, user=user, password=password, database=database)
    print("Conexão ao banco de dados realizada!")

    return bd

def fecha_bd(bd):
    bd.close()

def insere_aviao(bd, aviao, assentos):
    cursor = bd.cursor()

    try:
        sql = 'INSERT INTO aviao (num_serie, modelo) VALUES (%s, %s)'
        cursor.execute(sql, aviao)

        sql = 'INSERT INTO assento (tipo, num_serie_aviao) VALUES (%s, %s)'
        cursor.executemany(sql, assentos)

    except mysql.connector.Error as error:
        print(error)

    cursor.close()
    bd.commit()

def insere_aeroporto(bd, aeroporto):
    cursor = bd.cursor()

    try:
        sql = 'INSERT INTO aeroporto (nome, pais, estado, cidade) VALUES (%s, %s, %s, %s)'
        cursor.execute(sql, aeroporto)

    except mysql.connector.IntegrityError as error:
            print("Entrada duplicada para nome do aeroporto!")

    except mysql.connector.Error as error:
            print(error)

    cursor.close()
    bd.commit()

def insere_passageiro(bd, passageiro):
    cursor = bd.cursor()

    try:
        sql = 'INSERT INTO passageiro (rg, nome, passaporte, data_nascimento) VALUES (%s, %s, %s, %s)'
        cursor.execute(sql, passageiro)

    except mysql.connector.Error as error:
        print(error)

    cursor.close()
    bd.commit()

def insere_piloto(bd, piloto):
    cursor = bd.cursor()

    try:
        sql = 'INSERT INTO piloto (nome, passaporte, data_nascimento) VALUES (%s, %s, %s)'
        cursor.execute(sql, piloto)

    except mysql.connector.Error as error:
        print(error)

    cursor.close()
    bd.commit()

def gera_datas():
    ano = rd.randrange(2022, 2024)
    mes = rd.randrange(1, 13)
    dia = 0
    if (mes == 2):
        dia = rd.randrange(1, 29)
    else:
        dia = rd.randrange(1, 31)
    data_partida = dt.date(ano, mes, dia)

    dia = dia + 1
    if (mes == 2):
        if (dia >= 29):
            dia = 1
            mes += 1
    
    elif (dia >= 31):
        dia = 1
        if (mes == 12):
            mes = 1
            ano += 1

        else:
            mes += 1

    data_destino = dt.date(ano, mes, dia)

    return str(data_partida), str(data_destino)

def gera_horario():
    hora = rd.randrange(0, 24)
    minuto = rd.randrange(0, 60)
    segundo = rd.randrange(0, 60)

    horario = dt.time(hora, minuto, segundo)

    return str(horario)

def insere_passagens(bd):
    cursor = bd.cursor()

    info_voos = get_voos(bd)
    i = 0

    for cont_voo in range(len(info_voos)):
        voo = info_voos[i]
        cod_voo = voo[0]
        num_serie_aviao = voo[1]
        qtde_assentos = voo[2]
        qtde_assentos_gerados = rd.randrange(100, qtde_assentos + 1)
        cod_assentos = get_assentosaviao(bd, num_serie_aviao)

        assentos_ocupados = []
        passageiros_no_voo = []

        rg_passageiros = get_passageiros(bd)

        for cont_assento in range(qtde_assentos_gerados):
            passageiro = rg_passageiros[rd.randrange(0, len(rg_passageiros))]
            while(passageiro in passageiros_no_voo):
                passageiro = rg_passageiros[rd.randrange(0, len(rg_passageiros))]

            passageiros_no_voo.append(passageiro)
            
            assento = cod_assentos[rd.randrange(0, len(cod_assentos))]
            while(assento in assentos_ocupados):
                assento = cod_assentos[rd.randrange(0, len(cod_assentos))]

            assentos_ocupados.append(assento)

            passagem = (passageiro, assento, cod_voo)

            try:
                sql = 'INSERT INTO passagem (rg_passageiro, cod_assento, cod_voo) VALUES (%s, %s, %s)'
                cursor.execute(sql, passagem)

            except mysql.connector.Error as error:
                print(error)

        i += 1

    cursor.close()
    bd.commit()

def insere_voo(bd):
    cursor = bd.cursor()

    cod_pilotos = get_pilotos(bd)
    piloto = cod_pilotos[rd.randrange(0, len(cod_pilotos))]
    numserie_avioes = get_avioes(bd)
    aviao = numserie_avioes[rd.randrange(0, len(numserie_avioes))]
    cod_aeroportos = get_aeroportos(bd)
    aeroporto_partida = cod_aeroportos[rd.randrange(0, len(cod_aeroportos))]
    aeroporto_destino = cod_aeroportos[rd.randrange(0, len(cod_aeroportos))]
    while(aeroporto_destino == aeroporto_partida):
        aeroporto_destino = cod_aeroportos[rd.randrange(0, len(cod_aeroportos))]
    data_partida, data_destino = gera_datas()
    horario_partida = gera_horario()
    horario_destino = gera_horario()

    voo = (piloto, aviao, aeroporto_partida, aeroporto_destino, data_partida, horario_partida, data_destino, horario_destino)

    try:
        sql = 'INSERT INTO voo (cod_piloto, num_serie_aviao, cod_aeroporto_partida, cod_aeroporto_destino, data_partida, horario_partida, data_destino, horario_destino) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(sql, voo)

    except mysql.connector.Error as error:
        print(error)

    cursor.close()
    bd.commit()

def get_assentos(bd):
    cursor = bd.cursor()

    sql = 'SELECT codigo FROM assento'
    cursor.execute(sql)

    cod_assentos = []

    for codigo in cursor:
        cod_assentos.append(codigo[0])

    cursor.close()

    return cod_assentos

def get_passageiros(bd):
    cursor = bd.cursor()

    sql = 'SELECT rg FROM passageiro'
    cursor.execute(sql)

    rg_passageiros = []

    for rg in cursor:
        rg_passageiros.append(rg[0])

    cursor.close()

    return rg_passageiros

def get_pilotos(bd):
    cursor = bd.cursor()

    sql = 'SELECT codigo FROM piloto'
    cursor.execute(sql)

    cod_pilotos = []

    for codigo in cursor:
        cod_pilotos.append(codigo[0])

    cursor.close()

    return cod_pilotos

def get_avioes(bd):
    cursor = bd.cursor()

    sql = 'SELECT num_serie FROM aviao'
    cursor.execute(sql)

    numserie_avioes = []

    for numserie in cursor:
        numserie_avioes.append(numserie[0])

    cursor.close()

    return numserie_avioes

def get_aeroportos(bd):
    cursor = bd.cursor()

    sql = 'SELECT codigo FROM aeroporto'
    cursor.execute(sql)

    cod_aeroportos = []

    for codigo in cursor:
        cod_aeroportos.append(codigo[0])

    cursor.close()

    return cod_aeroportos

def get_voos(bd):
    cursor = bd.cursor()

    # codigo do voo, numero de serie do aviao e quantidade de assentos do aviao
    sql = 'SELECT v.codigo, v.num_serie_aviao, count(ast.codigo) FROM voo v JOIN aviao a ON a.num_serie = v.num_serie_aviao LEFT JOIN assento ast ON ast.num_serie_aviao = a.num_serie GROUP BY v.codigo'
    cursor.execute(sql)

    info_voos = []

    for info in cursor:
        info_voos.append(info)

    cursor.close()

    return info_voos

def get_assentosaviao(bd, num_serie_aviao):
    cursor = bd.cursor()

    sql = 'SELECT ast.codigo FROM aviao a JOIN voo v ON v.num_serie_aviao = a.num_serie JOIN assento ast ON ast.num_serie_aviao = a.num_serie WHERE a.num_serie = \'%s\'' % num_serie_aviao
    cursor.execute(sql)

    cod_assentos = []

    for codigo in cursor:
        cod_assentos.append(codigo[0])

    cursor.close()

    return cod_assentos