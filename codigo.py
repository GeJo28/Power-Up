import pyautogui
import time

pyautogui.PAUSE = 1

# pyautogui -> fazer automações com python

# Passo 1: Entrar no sistema  da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
    # abrir o chrome
pyautogui.press('win')
pyautogui.write('Edge')
pyautogui.press('enter')

    # digitar o site
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

    # espera 3 segundos
time.sleep(3)

# Passo 2: Fazer login
    # preencher o email
pyautogui.click(x=936, y=439)
pyautogui.write('joaovitor@gmail.com')

    # preencher a senha
pyautogui.press('tab')
pyautogui.write('123456789')

    # botão Logar
pyautogui.press('tab')
pyautogui.press('enter')

    # espera 3 segundos
time.sleep(3)

# Passo 3: Importar a base de dados
import pandas as pd

tabela_df = pd.read_csv('produtos.csv')

# Passo 4: Cadastrar todos os produtos
for linha in tabela_df.index: # para cada linha da minha tabela
    pyautogui.click(x=856, y=307)

    codigo = tabela_df.loc[linha, 'codigo']
    pyautogui.write(codigo)

    pyautogui.press('tab') # passar para o próximo campo
    marca = tabela_df.loc[linha, 'marca']
    pyautogui.write(marca)

    pyautogui.press('tab') # passar para o próximo campo
    tipo = tabela_df.loc[linha, 'tipo']
    pyautogui.write(tipo)

    pyautogui.press('tab') # passar para o próximo campo
    categoria = str(tabela_df.loc[linha, 'categoria'])
    pyautogui.write(categoria)

    pyautogui.press('tab') # passar para o próximo campo
    preco_unitario = str(tabela_df.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)

    pyautogui.press('tab') # passar para o próximo campo
    custo = str(tabela_df.loc[linha, 'custo'])
    pyautogui.write(custo)

    pyautogui.press('tab') # passar para o próximo campo
    obs = str(tabela_df.loc[linha, 'obs'])

    if obs != 'nan':
        pyautogui.write(obs)

    pyautogui.press('tab') # passar para o botão enviar
    pyautogui.press('enter')

    pyautogui.scroll(10000)