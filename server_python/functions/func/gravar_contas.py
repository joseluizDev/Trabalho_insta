

import os


def gravador_de_contas(nomeUser, senha):
    try:
        simp_path = r'relatorio de contas\\contas.txt'
        abs_path = os.path.abspath(simp_path)
        nome_arquivo = abs_path
        arquivo = open(nome_arquivo, 'r+')
    except FileNotFoundError:
        arquivo = open(nome_arquivo, 'w+')
    arquivo.close()
    f = open(abs_path, 'r')
    conteudo = f.readlines()
    conteudo.append(f'\n{nomeUser} {senha}')
    f2 = open(abs_path, 'w')
    f2.writelines(conteudo)
    f2 = open(abs_path, 'r')
    arquivo.close()
