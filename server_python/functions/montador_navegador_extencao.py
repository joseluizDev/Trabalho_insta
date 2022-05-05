from distutils import extension
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
import random
from subprocess import CREATE_NO_WINDOW
from functions.api.montar_por_api import Client_post
from functions.func.limpar_historico import limparlogins
from functions.func.open_json import ler_config_json
from functions.func.selecionar_pasta_de_fotos import selecionarlistadefotos
from instagrapi import Client

simp_path = r'config\\config.json'
abs_path = os.path.abspath(simp_path)
config = ler_config_json(abs_path)


def montador_extencao(config, user, senh):
    very = 0
    options = webdriver.ChromeOptions()
    if config["navegador"]["ocultar_navegador"]:
        options.add_argument("--headless")
    if config['navegador']['user_agent_aleatorio_mobile']:
        simp_path = r'config\\useragents_mobile.txt'
        abs_path = os.path.abspath(simp_path)
        with open(abs_path) as f:
            usermobi = [line.strip() for line in f if line.strip()]
        useragents = random.choice(usermobi)
        mobile_emulation = {"deviceMetrics": {
            "pixelRatio": 4.0}, "userAgent": useragents}
        options.add_experimental_option(
            "mobileEmulation", mobile_emulation)
    else:
        options.add_argument(
            f'user-agent={config["navegador"]["user_agent_fixo_mobile"]}')
    if config['navegador']['navegador_anonimo']:
        options.add_argument('--incognito')
    options.add_argument("--window-size=640,920")
    options.creationflags = CREATE_NO_WINDOW
    driver = webdriver.Chrome(
        executable_path=r'chromedriver.exe', options=options
    )

    driver.get('https://www.instagram.com/accounts/login/?next=/login/')
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_class_name(
            'cB_4K  ').click()
        sleep(4)
    except:
        pass
    driver.find_element_by_name('username').send_keys(user)
    sleep(0.1)
    driver.find_element_by_name('password').send_keys(senh)
    sleep(0.1)
    driver.find_element_by_name('password').click()
    driver.find_element_by_name('password').send_keys(Keys.ENTER)
    sleep(10)
    # foto de perfil
    bio = 0
    if config['montagem']['alterar_foto_de_perfil']:
        bio = 1
        driver.get('https://www.instagram.com/accounts/edit/')
        driver.implicitly_wait(10)
        fotos, pasta = selecionarlistadefotos(config)
        try:
            driver.find_element_by_class_name('tb_sK').send_keys(
                f'{pasta}\\{random.choice(fotos)}')
            sleep(2)
            driver.find_element_by_class_name('UP43G').click()
        except:
            pass
        sleep(3)
    # selecionar bio
    if config['montagem']['bioaleatoria']:
        ###########
        simp_path = r'config\\bio.txt'
        abs_path = os.path.abspath(simp_path)
        lista = []
        with open(abs_path, encoding='utf8') as infile:
            for i in infile.read().splitlines():
                lista.append(i)
        bio = str(random.choice(lista))

        driver.get('https://www.instagram.com/accounts/edit/')
        driver.implicitly_wait(10)
        sleep(1)
        driver.find_element_by_class_name('p7vTm').send_keys(bio)
        sleep(2)
        try:
            buttons = driver.find_elements_by_xpath(
                "//*[contains(text(), 'Enviar')]")
            for btn in buttons:
                btn.click()
        except:
            try:
                button = driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/article/form/div[10]/div/div/button')
                driver.execute_script("arguments[0].click();", button)
            except:
                try:
                    button = driver.find_element_by_xpath(
                        '/html/body/div[1]/section/main/div/article/form/div[10]/div/div/button')
                    driver.execute_script("arguments[0].click();", button)
                except:
                    pass
    sleep(2)
    c = 0
    simp_path = r'config\\legendas.txt'
    abs_path = os.path.abspath(simp_path)
    lista = []
    with open(abs_path, encoding='utf8') as infile:
        for i in infile.read().splitlines():
            lista.append(i)
    while True:
        c += 1
        try:
            if c == config['montagem']['qauntidade_de_fotos']:
                break
            driver.get(f'https://www.instagram.com/{user}/')
            driver.implicitly_wait(10)

            driver.execute_script(
                "HTMLInputElement.prototype.click = function() {                     " +
                "  if(this.type !== 'file') HTMLElement.prototype.click.call(this);  " +
                "};                                                                  ")
            try:
                driver.find_element_by_xpath(
                    '//div[@data-testid="new-post-button"]').click()
            except:
                driver.find_element_by_xpath(
                    "//div[@data-testid='new-post-button']/*[name()='svg']").click()

            driver.execute_script(
                "delete HTMLInputElement.prototype.click")
            driver.implicitly_wait(10)
            fotoss = random.choice(fotos)
            fotos.remove(fotoss)
            driver.find_element_by_class_name('tb_sK').send_keys(
                f'{pasta}\\{fotoss}')
            sleep(5)
            driver.find_element_by_class_name('UP43G').click()
            sleep(2)
            if config['montagem']['legenda']:
                legenda = str(random.choice(lista))
                try:
                    driver.find_element_by_class_name(
                        '_472V_').send_keys(legenda)
                    sleep(2)
                except:
                    driver.find_element_by_class_name(
                        '_472V_').send_keys(' ')
            driver.find_element_by_class_name('UP43G').click()
        except:
            very += 1
            if very == 4:
                break

            try:
                driver.find_element_by_class_name('cB_4K  ').click()
            except:
                pass
            # escolher um tempo aleatorio
        sleep(random.randint(
            config['montagem']['tempo_entre_postagem']['inicial'], config['montagem']['tempo_entre_postagem']['final']))
    if config['montagem']['postagen_de_story']['quantidade_fotos'] > 0 or config['montagem']['postagen_de_story']['quantidade_fotos'] > 0:
        clint = Client_post()
        clint.login(user, senh)
        if config['montagem']['postagen_de_story']['quantidade_fotos'] > 0:
            clint.postar_story(
                fotos, pasta, config=config)
        sleep(5)
        if config['montagem']['postagen_de_destaque']['quantidade_fotos'] > 0:
            clint.postar_destaque(config)
    # limpeza de login
    if config['montagem']['limpar_login']:
        limparlogins(driver)
    driver.quit()
