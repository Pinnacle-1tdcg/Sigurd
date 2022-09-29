import os
from unittest import skip
from pyfiglet import figlet_format
from time import sleep
from weakref import finalize
from fileinput import filename
import PySimpleGUI as sg
from PySimpleGUI import Window, Text, Image, theme_previewer

#BACKUP
extensoes = ['.txt', '.pdf', '.docx', '.xml', '.xbel', '.xls']
paths = [f"/home/{os.getlogin()}", "/root", "/tmp"] 

path_files = {"home": [], "root": [], "tmp": []}


# bloco de todas as funcoes que nosso programa esta utlizando

def apresentacao():

    print(figlet_format('Pinnacle'))

    print('Bem vindo ao software desenvolvido pelo time PINNACLE')
    print('Nosso objetivo é  manter seus arquivos e sua máquina mais seguros.')

def home(path = paths[0]):                                                                     # Esse bloco home, root, tmp servem para o programa fazer uma varredura nesses tres diretorios, buscando em cada pastas os arquivos que corresponderem as extensoes pre definidas, logo apos eles sao adicionados dentro da lista que fica dentro do dicionario.
    for root,dirs, files in os.walk(path):
        for x in files:
            fullPath = (root + "/" + x)
            arquivo, extensao = os.path.splitext(fullPath)
            if extensao in extensoes:
                path_files['home'].append("'" + arquivo + extensao + "'")

def root(path = paths[1]):
    for root,dirs, files in os.walk(path):
        for x in files: 
            fullPath = (root + "/" + x)
            arquivo, extensao = os.path.splitext(fullPath)
            if extensao in extensoes:
                path_files["root"].append("'" + arquivo + extensao + "'")

def tmp(path = paths[2]):
    for root,dirs, files in os.walk(path):
        for x in files: 
            fullPath = (root + "/" + x)
            arquivo, extensao = os.path.splitext(fullPath)
            if extensao in extensoes:
                path_files["tmp"].append("'" + arquivo + extensao + "'")

def pasta():                                                                                # Esse bloco serve para gerar nosso backup, ele ira criar uma pasta, e extrair as informacoes de cada lista e copiar para o novo diretorio, junto disso ela remove as permissoes da pasta deixando a somente para o root.
    os.popen('sudo mkdir backup /bin/"b@ck&ppinn@cl#" 2>/dev/null')
    for x in path_files['home']:
        os.popen(f'sudo cp {x} /bin/"b@ck&ppinn@cl#"/ 2>/dev/null')
    sleep(2)
    for x in path_files['root']:
        os.popen(f'sudo cp {x} /bin/"b@ck&ppinn@cl#"/ 2>/dev/null')
    sleep(2)
    for x in path_files['tmp']:
        os.popen(f'sudo cp {x} /bin/"b@ck&ppinn@cl#"/ 2>/dev/null')
    sleep(2)
    os.popen('sudo chmod 0 /bin/"b@ck&ppinn@cl#"/ ')

def teste_backup():
    apresentacao()
    home()
    root()
    tmp()
    pasta()

#JANELA
def janela_inicio():
    sg.theme('DarkGrey2')
    layout = [
        [Image(filename='logo.png')],
        [sg.Text("Olá seja bem vindo ao Anti-Ransomware PINNACLE")],
        [sg.Button("Continuar")],
        [sg.Text("")],
        [sg.Text("Copyright 2022 by Pinnacle - All rights reserved")],
    ]

    return sg.Window("PINNACLE - ANTI_RANSOMWARE", layout=layout, element_justification="c",icon="icon2.png", finalize = True)

def janela_funcao():
    sg.theme('DarkGrey2')
    layout = [

        [Image(filename='logo.png')],
        [sg.Text("Realize o Backup para proteger seu arquivos: ")],
        [sg.Button("Iniciar Backup"), sg.Button("Voltar")],
        [sg.Text("")],
        [sg.Text("Copyright 2022 by Pinnacle - All rights reserved")],
    ]

    return sg.Window("PINNACLE - ANTI_RANSOMWARE", layout=layout, element_justification="c", icon="icon2.png", finalize = True)

#criando a ordem das janelas
janela1, janela2 = janela_inicio(), None

#cirar loop de eventos
while True:
    window, evento, valores = sg.read_all_windows()
    if window == janela1 and evento == sg.WIN_CLOSED:
        break
    if window == janela2 and evento == sg.WIN_CLOSED:
        break
    if window == janela1 and evento == "Continuar":
        janela2 = janela_funcao()
        janela1.hide()
    if window == janela2 and evento == "Voltar":
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and evento == "Iniciar Backup":
        teste_backup()
        sg.popup("Backup realizado com sucesso!")
window.close()
