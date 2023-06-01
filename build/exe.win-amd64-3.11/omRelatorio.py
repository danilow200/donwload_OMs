from selenium import webdriver #importando o nevagador
from selenium.webdriver.common.by import By #serve para achar os elementos no navegador
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def baixar_relatorios(login, senha, os):
    ordens_servico = []
    ordens_servico.extend(os.split(","))

    url = "https://oss.telebras.com.br/cpqdom-web/login.xhtml"
    url_tabela = "https://oss.telebras.com.br/cpqdom-web/operation/OrderQueryList.xhtml"
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Maximiza a janela do navegador
    options.add_argument("--disable-extensions")  # Desativa as extensões do Chrome
    options.add_argument("--disable-gpu")  # Desativa a aceleração de hardware
    options.add_argument("--disable-dev-shm-usage")  # Desativa o uso compartilhado de memória /tmp
    options.add_argument("--no-sandbox")  # Desativa o sandbox do Chrome
    options.add_argument("--force-device-scale-factor=0.75")  # Define o zoom em 75%
    # options.add_argument("--headless")

    # diretorio_download = 'C:\\Users\\danilo.silva\\Documents\\test'

    # prefs = {
    #     "download.default_directory": diretorio_download,
    #     "download.prompt_for_download": False,
    #     "download.directory_upgrade": True,
    #     "safebrowsing.enabled": True
    # }
    # options.add_experimental_option("prefs", prefs)

    chrome = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
    chrome.get(url)
    time.sleep(2)

    elemento_usuario = chrome.find_element(By.XPATH, '/html/body/div[1]/form/div/table/tbody/tr[2]/td[3]/input')
    elemento_usuario.send_keys(login)
    elemento_senha = chrome.find_element(By.XPATH, '/html/body/div[1]/form/div/table/tbody/tr[3]/td[3]/input')
    elemento_senha.send_keys(senha)
    elemento_entrar = chrome.find_element(By.XPATH, '/html/body/div[1]/form/div/table/tbody/tr[5]/td[3]/button')
    elemento_entrar.send_keys(Keys.RETURN)

    time.sleep(1)

    for ordem_servico in ordens_servico:
        chrome.get(url_tabela)
        elemento_filtro = chrome.find_element(By.XPATH, '/html/body/form[2]/div/div/div/div/div[2]/div/table/thead/tr/th[1]/input')
        elemento_filtro.clear()
        elemento_filtro.send_keys(ordem_servico)
        time.sleep(2)
        chrome.find_element(By.XPATH, '/html/body/form[2]/div/div/div/div/div[3]/table/tbody/tr/td[1]').click()
        time.sleep(2)
        chrome.find_element(By.XPATH, '/html/body/form[1]/div/div/div[2]/button[1]').click()
        time.sleep(2)
        chrome.find_element(By.XPATH, '/html/body/form[1]/div[3]/ul/li[4]/a').click()
        time.sleep(1)

        Botão_existe = chrome.find_elements(By.XPATH, '/html/body/form[1]/div[3]/div/div[4]/div/div[2]/table/tbody/tr/td[8]/button[1]')
        if len(Botão_existe) == 0: #checa se a tabela e a estação foram carregados na página
            while True: #roda loop até que ela seja carregada
                chrome.refresh() #recarregar página do navegador
                time.sleep(2)
                chrome.find_element(By.XPATH, '/html/body/form[1]/div/div/div[2]/button[1]').click()
                time.sleep(2)
                chrome.find_element(By.XPATH, '/html/body/form[1]/div[3]/ul/li[4]/a').click()
                time.sleep(1)
                Botão_existe = chrome.find_elements(By.XPATH, '/html/body/form[1]/div[3]/div/div[4]/div/div[2]/table/tbody/tr/td[8]/button[1]')
                if len(Botão_existe) > 0: #para o loop quando a tabela for carregada
                    break

        chrome.find_element(By.XPATH, '/html/body/form[1]/div[3]/div/div[4]/div/div[2]/table/tbody/tr/td[8]/button[1]').click()
        time.sleep(3)