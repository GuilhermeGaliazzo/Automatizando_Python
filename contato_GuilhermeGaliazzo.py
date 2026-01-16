import pyautogui, pyperclip
import time
pyautogui.PAUSE = 2


link = "http://gmail.com/"
corpo = "Bom dia! Quero entrar em contato com você. Quais são seus endereços de contato?"

#Automação pode não funcionar caso seu monitor seja de tamanho/resolução diferente do meu ou caso não 
#tenha o navegador usado na automação(Microsoft Edge)

#Acessar o navegador
pyautogui.press("win")
pyautogui.write("Microsoft Edge")
pyautogui.press("enter")
pyautogui.click(pyautogui.position(x=641, y=58))

#Acessar o email
pyautogui.write(link)
pyautogui.press("enter")

#Seleciona o destinatário (Guilherme Galiazzo) 
pyautogui.click(pyautogui.position(x=78, y=172))
pyautogui.write("guilhermemassari.rodrigues@gmail.com")
pyautogui.click(pyautogui.position(x=1377, y=584))

#Digita o assunto
pyautogui.click(pyautogui.position(1302, 513))
pyautogui.write("Entrar em contato")

#Digita no corpo do email
pyautogui.click(pyautogui.position(1301, 563))
pyperclip.copy(corpo)
pyautogui.hotkey("ctrl", "v")

#Envia
pyautogui.click(pyautogui.position(x=1301, y=994))