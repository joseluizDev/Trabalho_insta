import os
import random


def selecionarlistadefotos(config):
    fotos = []
    pastas = []

    simp_path = r'fotos'
    abs_path = os.path.abspath(simp_path)
    if config['criacao']['genero'] == 'F':
        count = 0
        abs_path = abs_path+"\\femenino"
        for diretorio, subpastas, arquivos in os.walk(abs_path):
            count += 1
            pastas.append(subpastas)
        pasta = f'{abs_path}\\{pastas[0][random.randint(0, len(pastas[0])-1)]}'
        for arquivo in os.walk(pasta):
            if arquivo[-4:] == '.jpg' or '.png' or '.jpeg':
                fotos.append(arquivo)
    else:
        count = 0
        abs_path = abs_path+"\\masculino"
        for diretorio, subpastas, arquivos in os.walk(abs_path):
            count += 1
            pastas.append(subpastas)
        pasta = f'{abs_path}\\{pastas[0][random.randint(0, len(pastas[0])-1)]}'
        for arquivo in os.walk(pasta):
            if arquivo[-4:] == '.jpg' or '.png' or '.jpeg':
                fotos.append(arquivo)
    return fotos[0][2], pasta
