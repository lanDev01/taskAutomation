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

time.sleep(5)