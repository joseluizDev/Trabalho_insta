from distutils.command.config import config
from instagrapi import Client
from http import client
import os
import random
from time import sleep


class Client_post:
    def __init__(self):
        self.username = ""
        self. password = ""
        self.clint = Client()

    def login(self, username, password):
        self.username = username
        self.password = password
        self.clint.login(username=self.username, password=self.password)

    def postar_story(self,  fotos, pasta, config):
        lista = []
        simp_path = r'config\\legendas.txt'
        abs_path = os.path.abspath(simp_path)
        with open(abs_path, encoding='utf8') as infile:
            for i in infile.read().splitlines():
                lista.append(i)
        for i in range(config["montagem"]["postagen_de_story"]["quantidade_fotos"]):
            legenda = str(random.choice(lista))
            fot = random.choice(fotos)
            self.clint.photo_upload_to_story(f"{pasta}\\{fot}", legenda)
            sleep(random.randint(
                config['montagem']["postagen_de_story"]["tempo_inicial"], config['montagem']["postagen_de_story"]["tempo_final"]))

    def postar_destaque(self, config):
        lista = []
        simp_path = r'config\\nomes_f.txt'
        abs_path = os.path.abspath(simp_path)
        with open(abs_path, encoding='utf8') as infile:
            for i in infile.read().splitlines():
                lista.append(i)
        for i in range(config["montagem"]["postagen_de_destaque"]["quantidade_fotos"]):
            story = self.clint.user_stories(self.clint.user_id)
            try:
                self.clint.highlight_create(
                    title=random.choice(lista), story_ids=[story[i].pk],)
            except:
                pass
            sleep(random.randint(
                config['montagem']["postagen_de_destaque"]["tempo_inicial"], config['montagem']["postagen_de_destaque"]["tempo_final"]))
