# Passo 1 - Abrir o navegador e digitar o endereço
# Passo 2 - Inserir o usúario, senha e apertar enter
# Passo 3 - No menu selecionar o acesso
# Passo 4 - Na pagina de serviços selecionar a opção relatorios
# Passo 5 - Selecionar o opção consultar serviço
# Passo 6 - Na pagina de consulta selecionar o input "instalação" inserir a instalação e apertar enter.
# Passo 7 - Caso não tenha informação a pagina emiti um alerta onde será necessario apertar enter "FIM do processo"
# Passo 8 -


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from time import sleep

## Navegador
navegador = webdriver.Chrome()
navegador.get("https://acessodigitalforn.neoenergia.com/logon/LogonPoint/tmindex.html")

## Realizando login na pagina

inputLogin = '//*[@id="login"]'
inputSenha = '//*[@id="passwd"]'
bottonEntrar = '//*[@id="nsg-x1-logon-button"]'

inputElementLogin = navegador.find_element_by_xpath(inputLogin)
inputElementLogin.click()
inputElementLogin.send_keys('xxxxxxx')
inputElementSenha = navegador.find_element_by_xpath(inputSenha)
inputElementSenha.click()
inputElementSenha.send_keys('xxxxx')
bottonElementEntrar = navegador.find_element_by_id(bottonEntrar)
bottonElementEntrar.send_keys(Keys.ENTER)