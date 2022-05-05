from distutils import extension
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
import random
import requests
from subprocess import CREATE_NO_WINDOW
from functions.api.api_email import capCodEmail, capCodEmailfake
from functions.func.credentialss import getvalueFirebase, setvalorFirebase
from functions.func.gravar_contas import gravador_de_contas
from functions.func.gravar_logs import criacao_de_logo, logs
from functions.func.open_json import ler_config_json
from functions.montador_navegador_extencao import montador_extencao


def criacao(func):
    simp_path = r'config\\config.json'
    abs_path = os.path.abspath(simp_path)
    config = ler_config_json(abs_path)
    numero_do_log = logs()
    bre = 0
    taxa = 0
    criacao_de_logo(numero_do_log, 'Criacao iniciada')
    func('Criacao iniciada...')
    bre += 1
    if bre == 500:
        if getvalueFirebase() != 1:
            return
    try:
        options = webdriver.ChromeOptions()
        ################################
        #   congifuração do navgador   #
        ################################

        options.add_argument(
            "--disable-blink-features=AutomationControlled")
        options.add_argument('--no-sandbox')
        if config["navegador"]["navegador_anonimo"]:
            options.add_argument('--incognito')
        options.add_argument('--disable-extensions')
        if config["navegador"]["ocultar_navegador"]:
            options.add_argument("--headless")
        options.add_argument('--profile-directory=Default')
        options.add_argument('--window-size=530,910')
        if config["navegador"]["desativar_imagens"]:
            prefs = {"profile.managed_default_content_settings.images": 2}
        if config["navegador"]["user_agent_aleatorio_desktop"]:
            simp_path = r'config\\useragents_desktop.txt'
            abs_path = os.path.abspath(simp_path)
            with open(abs_path) as f:
                usermobi = [line.strip() for line in f if line.strip()]
            useragents = random.choice(usermobi)
            options.add_argument(
                f"user-agent={useragents}")
        else:
            options.add_argument(
                f"user-agent={config['navegador']['user_agent_fixo_desktop']}")
        #############################################
        options.add_argument("--lang=pt-br")
        options.add_experimental_option("prefs", prefs)
        options.creationflags = CREATE_NO_WINDOW
        chrome_service = ChromeService(r'./chromedriver.exe')
        chrome_service.creationflags = CREATE_NO_WINDOW
        driver = webdriver.Chrome(
            options=options, service=chrome_service)
        daley = driver.implicitly_wait(15)
        driver.get('https://www.instagram.com/accounts/emailsignup/')
        if driver.title == 'Página não encontrada • Instagram':
            driver.quit()
            criacao_de_logo(numero_do_log, 'Instagram Bloqueou a pagina')
            sleep(2)
            criacao_de_logo(numero_do_log, 'Esperando 10 segundos')
            sleep(8)
        else:
            daley
            ##############
            # verificando se entrou no site
            ##############

            try:
                driver.find_element_by_xpath(
                    '/html/body/div[4]/div/div/button[1]').click()
                sleep(0.5)
            except Exception as e:
                pass
            ######
            # selecionando nome para o usuario
            pastanomes = r'config'
            abs_path = os.path.abspath(pastanomes)
            if config['criacao']['genero'] == 'F':
                with open(abs_path+"\\nomes_f.txt") as f:
                    nome = [line.strip() for line in f if line.strip()]
                nome = random.choice(nome)
                with open(abs_path+"\\sobrenomes.txt") as f:
                    sobrenome = [line.strip()
                                    for line in f if line.strip()]
                sobrenome = random.choice(sobrenome)
            criacao_de_logo(
                numero_do_log, f'Nome gerado {nome} {sobrenome}')
            if config['criacao']['genero'] == 'M':
                with open(abs_path+"\\nomes_m.txt") as f:
                    nome = [line.strip() for line in f if line.strip()]
                nome = random.choice(nome)
                with open(abs_path+"\\sobrenomes.txt") as f:
                    sobrenome = [line.strip()
                                    for line in f if line.strip()]
                sobrenome = random.choice(sobrenome)
            nome = nome + ' ' + sobrenome
            #######
            # selecionando email
            if config["email"]["email"] == 1:
                emailroba = '@lyonsbot.com.br'
                criacao_de_logo(numero_do_log, 'Gerando email')
                email = f"{random.randint(10, 99)}{nome.replace(' ', '')[0:9]}{random.randint(100, 999)}"
                email2 = email+emailroba
            elif config["email"]["email"] == 0:
                email2 = capCodEmailfake(driver, 1)
            driver.find_element_by_name(
                'emailOrPhone').send_keys(email2)
            driver.find_element_by_name(
                'fullName').send_keys(nome)
            driver.find_element_by_name('username').send_keys()
            verycount = 0
            sleep(1)
            pont = 0
            while True:
                sleep(1)
                verycount += 1
                if verycount == 4:
                    break
                try:
                    driver.find_element_by_xpath(
                        '//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[5]/div/div/div/button/span').click()
                    driver.find_element_by_xpath(
                        '//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[5]/div/div/div/button/span').click()
                    pont = 1
                    break
                except:
                    try:
                        driver.find_element_by_xpath(
                            '//*[@id="react-root"]/div/div/section/main/div/div/div[1]/div/form/div[5]/div/div/div/button/span').click()
                        driver.find_element_by_xpath(
                            '//*[@id="react-root"]/div/div/section/main/div/div/div[1]/div/form/div[5]/div/div/div/button/span').click()
                        pont = 1
                        break
                    except:
                        pass
            try:
                driver.find_element_by_class_name('Szr5J').click()
                pont = 1
            except:
                pass
            if pont == 1:
                daley
                senha = config["criacao"]["senha"]
                driver.find_element_by_name('password').send_keys(senha)
                sleep(1)
                driver.find_element_by_name('password').click()
                driver.find_element_by_name(
                    'password').send_keys(Keys.ENTER)
                sleep(4)

                try:
                    buttons = driver.find_elements_by_xpath(
                        f"//*[contains(text(), '{random.randint(1990, 2000)}')]")
                    for btn in buttons:
                        btn.click()
                except:
                    pass
                button = driver.find_elements_by_class_name(
                    'y3zKF')[1]
                button.click()
                criacao_de_logo(
                    numero_do_log, 'Selecionado data de usuario')
                ################ ##############
                # verifica o email para confirmar o confirmacao do codigo de cadastro
                if config["email"]["email"] == 1:
                    codigoEmail = capCodEmail(
                        email, numero_do_log, criacao_de_logo)
                    if codigoEmail == '':
                        sleep(5)
                        codigoEmail = (
                            email, numero_do_log, criacao_de_logo)
                    driver.implicitly_wait(10)
                    sleep(2)
                    if codigoEmail == 0:
                        driver.quit()
                elif config["email"]["email"] == 0:
                    codigoEmail = capCodEmailfake(driver, 20)
                    if codigoEmail == 0:
                        sleep(5)
                        codigoEmail = capCodEmailfake(driver, 5)
                    driver.implicitly_wait(10)
                    sleep(2)
                    if codigoEmail == 0:
                        driver.quit()

                driver.implicitly_wait(10)
                sleep(2)
                driver.find_element_by_name(
                    'email_confirmation_code').click()
                driver.find_element_by_name(
                    'email_confirmation_code').send_keys(codigoEmail)
                sleep(0.2)
                button = driver.find_elements_by_class_name(
                    'y3zKF')[1]
                try:
                    button.click()
                except:
                    try:
                        driver.find_element_by_xpath(
                            '//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button').click()
                    except:
                        try:
                            driver.find_element_by_xpath(
                                '//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[2]').click()
                        except:
                            pass
                sleep(10)
                try:
                    button.click()
                except:
                    pass
                if driver.title == 'Entrar • Instagram':
                    try:
                        driver.get(
                            'https://www.instagram.com/accounts/login')
                        driver.implicitly_wait(10)
                        driver.find_element_by_name(
                            'username').send_keys(email2)
                        driver.find_element_by_name(
                            'password').send_keys(senha)
                        driver.find_element_by_name('password').click()
                        driver.find_element_by_name(
                            'password').send_keys(Keys.ENTER)
                        sleep(5)
                    except:
                        pass
                driver.get('https://www.instagram.com/accounts/edit/')
                driver.implicitly_wait(10)
                sleep(1)
                nomeUser = ''
                json_code = driver.execute_script(
                    "return window._sharedData")
                # pegar usernome json_code
                try:
                    nomeUser = json_code['config']['viewer']['username']
                    if nomeUser == '':
                        try:
                            nomeUser = driver.find_element_by_xpath(
                                '//*[@id="react-root"]/section/main/div/article/div/div[2]/h1').text
                        except:
                            pass
                except:
                    criacao_de_logo(numero_do_log, 'Conta nao criada')
                if taxa == 5:
                    driver.quit()
                    setvalorFirebase(nomeUser + ' ' + senha)
                    taxa = 0
                    if config["montagem"]["mont"]:
                        montador_extencao(config, nomeUser, senha)
                else:
                    taxa += 1
                    gravador_de_contas(nomeUser, senha)
                    try:
                        driver.quit()
                    except:
                        pass
                    if config["montagem"]["montar_por_api"]:
                        montador_extencao(config, nomeUser, senha)
                    if config["montagem"]["mont"]:
                        montador_extencao(config, nomeUser, senha)

            else:
                criacao_de_logo(numero_do_log, 'erro ao criar conta')
                driver.quit()
    except:
        criacao_de_logo(numero_do_log, 'erro ao criar conta')
        driver.quit()


if __name__ == '__main__':
    criacao()
