from asyncio import sleep
import requests


def capCodEmail(email, num, criacao_de_logo):
    ######
    criacao_de_logo(num, 'esperando codigo')
    count = 0
    while True:
        count += 1
        try:
            sleep(4)
            if count == 10:
                return 0
            response = requests.get(
                f'https://lyonsbot.com.br/api/messages/{email}/yvEW5xKHliptoAeY3LZw')
            codigodados = response.json()
            try:
                if codigodados[0]['sender_name'] == 'Instagram':
                    criacao_de_logo(num, 'codigo recebido')
                    criacao_de_logo(num, codigodados[0]['subject'].split()[0])
                    return codigodados[0]['subject'].split()[0]
            except:
                pass
        except:
            pass


def capCodEmailfake(driver, temp):
    try:
        email = ''
        codigoinsta = 0
        if temp == 1:
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get('https://www.fakemail.net/')
            driver.implicitly_wait(10)
            if driver.title != 'FakeMail | Temp Mail Addresses':
                driver.get('https://www.fakemail.net/')
                driver.implicitly_wait(10)
            email = driver.find_element_by_class_name('animace').text
            driver.switch_to.window(driver.window_handles[0])
        else:
            driver.switch_to.window(driver.window_handles[1])
            count = 0
            while True:
                count += 1
                if count == temp:
                    break
                sleep(1.5)
                codigo = driver.find_element_by_id('schranka').text
                codigo = codigo.split()
                if codigo[0] == '"Instagram"':
                    codigoinsta = codigo[1]
                if codigoinsta != 0:
                    driver.close()
                    break
                driver.refresh()
            driver.switch_to.window(driver.window_handles[0])

        if codigoinsta != 0:
            return codigoinsta
        elif email != '':
            return email
    except:
        return 0
