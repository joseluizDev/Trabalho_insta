from time import sleep


def limparlogins(driver):
    try:
        driver.get('https://www.instagram.com/session/login_activity/')
        try:
            driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div[3]/div[2]/button').click()
            sleep(4)
        except:
            pass
        driver.implicitly_wait(5)
        try:
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div/div[6]/div/div/button').click()
        except:
            pass
        limp = 7
        while True:

            if limp == 0:
                break
            try:
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                driver.implicitly_wait(5)
                driver.find_element_by_xpath(
                    f'/html/body/div[1]/section/main/div/article/div/div/div[3]/div[{limp}]').click()
                driver.implicitly_wait(5)
                driver.find_element_by_xpath(
                    '/html/body/div[5]/div/div/div[2]/div[2]/div/div[2]/button/div').click()
                driver.implicitly_wait(5)
                driver.find_element_by_xpath(
                    '/html/body/div[6]/div/div/div/div[2]/button[2]').click()
                limp -= 1
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
            except:
                limp -= 1
    except:
        pass
