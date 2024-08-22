import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

# Solicita ao usuário o código da ação desejada
ticker = input("Digite o código da ação desejada: ")

# Obtém os dados históricos de preço de fechamento da ação para o ano de 2020
dados = yfinance.Ticker(ticker).history(start="2020-01-01", end="2020-12-31")
fechamento = dados.Close

# Calcula as estatísticas: preço máximo, mínimo e médio de fechamento
maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

# Define os detalhes do e-mail
destinatario = "netolb360@gmail.com"
assunto = "Análise do projeto 2020"

# Cria a mensagem do e-mail com as análises calculadas
mensagem = f"""
Prezado,

Seguem as análises solicitadas da ação {ticker}:

Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Valor médio: R${valor_medio}

Qualquer dúvida, estou à disposição!
"""

# Abre o Gmail no navegador padrão
webbrowser.open("https://www.gmail.com")
time.sleep(5)  # Aguarda 5 segundos para o Gmail carregar

# Configura a pausa entre os comandos do pyautogui
pyautogui.PAUSE = 4

# Clica no botão de composição de e-mail (as coordenadas podem precisar de ajuste)
pyautogui.click(x=89, y=159)

# Copia e cola o destinatário no campo de "Para:"
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")  # Move para o próximo campo

# Copia e cola o assunto no campo de "Assunto:"
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")  # Move para o próximo campo

# Copia e cola a mensagem no corpo do e-mail
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# Clica no botão de enviar (as coordenadas podem precisar de ajuste)
pyautogui.click(x=784, y=832)
