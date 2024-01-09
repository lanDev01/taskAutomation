import pyautogui
import pandas
import time

# o PAUSE da um tempo de 1 segundo entre um comando e outro
pyautogui.PAUSE = 1

# press aperta uma tecla
# write escreve
# o click -> clica
# hotkey cria um atalho
# scroll -> rolar a tela

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Acessando URL no navegador
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(2)

# fazendo login
pyautogui.click(x=3420, y=463)

pyautogui.write("lnjnr9215@gmail.com") # escrevendo a senha
pyautogui.press("tab") # pulando para proximo campo
pyautogui.write("alan123456") # escrevendo a senha
pyautogui.press("tab")
pyautogui.press("enter") # apertando enter
time.sleep(3)

# importar a base de dados

table = pandas.read_csv("produtos.csv")

# Cadatrando produtos
for line in table.index:
    # Clicando no primeiro campo | input
    pyautogui.click(x=3453, y=316)

    # Codigo
    pyautogui.write(table.loc[line, "codigo"])
    pyautogui.press("tab")
    # marca
    pyautogui.write(table.loc[line, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(table.loc[line, "tipo"])
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(table.loc[line, "categoria"])) # converter para string
    pyautogui.press("tab")
    # preco
    pyautogui.write(str(table.loc[line, "preco_unitario"])) # converter para string
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(table.loc[line, "custo"])) # converter para string
    pyautogui.press("tab")
    # obs
    obs = table.loc[line, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    # enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")

    # Dando um scroll até o inicio da tela
    pyautogui.scroll(5000)