#!/usr/bin/env python
# coding: utf-8

# # Automação de ERPs
# 
# Sistema ERP = O planejamento de recursos empresariais (ERP) é um sistema de software que ajuda você a administrar toda a empresa, oferecendo suporte à automação e aos processos de finanças, recursos humanos, produção, cadeia de suprimentos, serviços, procurement e muito mais.
# 
# #### Biblioteca pyautogui
# Por meio da biblioteca pyautogui é possível integrar, a fim de automatizar, o Python a Sistemas ERPs (SAP, Totvs). Dessa forma, o Python consegue acessar o programa do sistema via Desktop.
# 
# #### Sistema ERP Fakturama
# O Fakturama é um exemplo de sistema ERP gratuito, que será usado neste projeto. O aplicativo está salvo na unidade D.
# 
# #### Desafio:
# A partir de um banco de dados de produtos (Produtos - Revisao.xlsx), cadastrar estes produtos no sistema ERP (Fakturama).

# In[1]:


import pyautogui as gui
import pandas as pd
import time
import pyperclip


# ##### Importar a base de dados

# In[2]:


df = pd.read_excel('Produtos - Revisao.xlsx')
display(df)
df.info()


# In[3]:


# tratamento de dados necessário para o correto preenchimento das informações no fakturama
df['Custo'] = df['Custo'].astype(str)
df['Custo'] = df['Custo'].str.replace('.', ',')

display(df)


# ##### Configurar o pyautogui

# In[4]:


gui.PAUSE = 0.5
gui.FAILSAFE = True
gui.alert('AUTOMAÇÃO INICIADA! Não tocar no mouse e teclado.')


# ##### Abrir o Fakturama

# In[5]:


# abrir o fakturama
gui.press('win')
gui.write('fakturama')
gui.press('enter')

# função para carregar imagens
def carregar_imagem(imagem):
    while not gui.locateOnScreen(imagem, grayscale=True, confidence=0.9):
        time.sleep(1)
    x, y, largura, altura = gui.locateOnScreen(imagem, grayscale=True, confidence=0.9)
    return x, y, largura, altura

# aguardar o carregamento do fakturama
logo = carregar_imagem('Prints\Screenshot_1.png')


# ###### Adicionar os produtos ao ERP

# In[6]:


for linha in df.index:
    
        # clicar em adicionar produto
        new_product = carregar_imagem('Prints\Screenshot_2.png')
        gui.click(gui.center(new_product))

        # selecionar item number
        gui.press(['tab', 'tab', 'tab', 'tab', 'tab', 'tab']) 

        # definir as informações a serem repassadas
        item_number = str(df.loc[linha, 'Código'])
        name = df.loc[linha, 'Nome']
        category = df.loc[linha, 'Categoria']
        gtin = str(df.loc[linha, 'GTIN'])
        supplier_code = str(df.loc[linha, 'Fornecedor'])
        description = df.loc[linha, 'Descrição']
        price = str(f"{df.loc[linha, 'Preço']},00")
        cost_price = str(f"{df.loc[linha, 'Custo']},00")
        stock = str(f"{df.loc[linha, 'Estoque']},00")

        # preencher 
        gui.write(item_number)
        gui.press('tab')
        
        pyperclip.copy(name)
        gui.hotkey('ctrl', 'v')
        gui.press('tab')
        
        gui.write(category)
        gui.press('tab') 
        
        gui.write(gtin)
        gui.press('tab')
        
        gui.write(supplier_code)
        gui.press('tab')
        
        pyperclip.copy(description)
        gui.hotkey('ctrl', 'v')
        gui.press('tab')
        
        gui.write(price)
        gui.press('tab') 
        
        gui.write(cost_price)
        gui.press(['tab', 'tab', 'tab'])
        
        gui.write(stock)
        gui.press(['tab', 'tab', 'tab', 'tab'])     
        gui.press('enter')
        
        # selecionar a imagem .png
        name = name.lower()
        pyperclip.copy(name)
        gui.hotkey('ctrl', 'v')
        gui.press('enter')
        
        # clicar em save
        save = carregar_imagem('Prints\Screenshot_4.png')
        gui.click(gui.center(save))
        
        print(f'{name} salvo!')


# In[7]:


# fechar o Fakturama
gui.hotkey('alt', 'f4')
gui.alert('A automação foi concluida!')

