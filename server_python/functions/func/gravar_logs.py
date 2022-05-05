import os
from datetime import datetime

#######
# retorna o numero do bot


def logs():
    output = os.popen('wmic process get description').read()
    lista = output.split('\n')
    count = 0
    for i in range(0, len(lista)):
        if 'criador.exe' in lista[i]:
            count += 1
    return int(count/2)


# grava na lista de dados


def criacao_de_logo(numbers, logs):

    data = datetime.today().strftime('%H:%M:%S')
    try:
        simp_path = r'logs\\log_de_criacao.txt'
        abs_path = os.path.abspath(simp_path)
        nome_arquivo = abs_path
        arquivo = open(nome_arquivo, 'r+')
    except FileNotFoundError:
        arquivo = open(nome_arquivo, 'w+')
    arquivo.close()
    f = open(abs_path, 'r')
    conteudo = f.readlines()

    conteudo.append(f'\n{numbers}-{data}-{logs}')
    f2 = open(abs_path, 'w')
    f2.writelines(conteudo)
    f2 = open(abs_path, 'r')
    arquivo.close()


criacao_de_logo(1, 'Criado')
