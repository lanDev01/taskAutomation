import pyautogui
import time

# o PAUSE da um tempo de 1 segundo entre um comando e outro
pyautogui.PAUSE = 1

# press aperta uma tecla
# write escreve
# hotkey cria um atalho
# o click -> clica

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