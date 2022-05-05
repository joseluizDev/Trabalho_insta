import os
import os
import random
import shutil


def selecionarlistadefotos():
    fotos = []
    pastas = []
    simp_path = r'central'
    abs_path = os.path.abspath(simp_path)
    count = 0
    for diretorio, subpastas, arquivos in os.walk(abs_path):
        count += 1
        pastas.append(subpastas)
    pasta = f'{abs_path}\\{pastas[0][random.randint(0, len(pastas[0])-1)]}'
    for arquivo in os.walk(pasta):
        if arquivo[-4:] == '.jpg' or '.png' or '.jpeg':
            fotos.append(arquivo)
    return fotos[0][2], pasta


def mover_fotos_aleatorias(pasta_origem, pasta_destino):
    #editar fotos
    for foto in pasta_origem[0]:
        print(foto)
        shutil.move(pasta_origem[1] + '\\' + foto, pasta_destino)


mover_fotos_aleatorias(selecionarlistadefotos(), 'edicao')
