import os
from time import sleep
from unittest import skip
from pyfiglet import figlet_format
import psutil
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno
import multiprocessing
import datetime
import time
from py_essentials import hashing as hs

hashs = ['f864922f947a6bb7d894245b53795b54b9378c0f7633c521240488e86f60c2c5', 'e29aa629bf492a087a17fa7ec0edb6be4b84c5c8b0798857939d8824fa91dbf9a']

hashes_seguras_armadilha = []



def armadilha():
    """Criacao da pasta armadilha, cria uma pasta, e cria 50 arquivos .txt dentro dela."""
    os.popen('mkdir /armadilha 2>/dev/null')
    sleep(2)
    for x in range(0,50):
        with open(f"/armadilha/pinnacle{x}.txt", 'w') as file:
            file.write("We catch you.")
    for root, dirs, files in os.walk('/armadilha'):
        for file in files:
            fullpath = root + '/' + file 
            hashes = hs.fileChecksum(fullpath, 'sha256')
            hashes_seguras_armadilha.append(hashes)
    sleep(1)
    os.popen(f"sudo ln -sf /armadilha /bin/armadilha && ln -sf /armadilha /root/armadilha && ln -sf /armadilha /usr/armadilha && ln -sf /armadilha /tmp/armadilha && /armadilha /home/{os.getlogin()} 2>/dev/null")

def detector_finalizador():
    """Usando de base a pasta criada na funcao armadilha(), faz monitoramento na pasta procurando por alguma mudança, o principal valor que acontece é sua .txt ser mudada, com isso o codigo executa e busca os processos do computador e mata os mais recentes."""
    while True:
        for root, dirs, files in os.walk("/armadilha"):
            for file in files:
                fullpath = (root + '/' + file)
                arquivo, extensao = os.path.splitext(fullpath)
                try:
                    verificacao = hs.fileChecksum(fullpath, 'sha256')
                except:
                    pass

                sleep(0.1)

                if extensao != ".txt":
                    print("RANSOMWARE DETECTADO, INICIANDO MEDIDAS DE SEGURANÇA.")
                    os.popen("rm -rf /armadilha")
                    sleep(2)

                    os.popen(f"killall -u {os.getlogin()}")
                
                elif verificacao not in hashes_seguras_armadilha:
                    print('Ransomware Detectado.')
                    os.popen('rm -rf /armadilha')
                    os.popen(f'killall -u {os.getlogin()}')


def cpu_usage():


    while True:

        porcetagem = psutil.cpu_percent(4)

        if porcetagem < 20:

            root = tk.Tk()
            root.title("Pinnacle Anti-Ransomware")
            root.geometry("350x150")

            def confirma():

                answer = askyesno(title="Pinnacle Anti-Ransomware",
                                message=f"{os.getlogin()} é voce quem esta fazendo uma tarefa extremamente pesada no computador? pergunta extremamente critica seu sistema pode estar sob ataque.")
                
                if answer == False:
                    print("RANSOMWARE DETECTADO, INICIANDO MEDIDAS DE SEGURANÇA.")
                    os.popen("sudo rm -rf /armadilha")
                    sleep(2)

                    os.popen(f'killall -u {os.getlogin()}')

                
                
            ttk.Button(
                root,
                text="CONFIRMAÇÃO",
                command=confirma).pack(expand=True)
            
            root.mainloop()
        sleep(1800)

def inodes():
    while True:
        validacao1 = os.statvfs("/").f_favail
        sleep(2)
        validacao2 = os.statvfs("/").f_favail
        diferenca = abs(validacao1 - validacao2)
        if diferenca > 1000000:
            print("Ransomwore detectado, iniciando medidas de proteção.")
            os.popen(f"killall -u {os.getlogin()}")

def hash_analizer(): 
    """Analisar hashs de arquivos que estao na pasta de downloads e ver se bate com as pre definidas na lista."""


    while True:
        for root, dirs, files in os.walk(f"/home/{os.getlogin()}/Downloads/"):
            for file in files:
                fullpath = root + '/' + file
                try:
                    hash = hs.fileChecksum(fullpath, 'sha256')
                except:
                    pass
                sleep(2)
                if hash in hashs:
                    print(hash)
                    print("Hash de um arquivo malicioso foi detectado, o arquivo sera excluido.")
                    os.popen(f'rm {fullpath}')
                    sleep(1)
                    os.popen(f"killall -u {os.getlogin()}")

armadilha()


if __name__ == "__main__":
    process1 = multiprocessing.Process(target=detector_finalizador)
    process2 = multiprocessing.Process(target=cpu_usage)
    process3 = multiprocessing.Process(target=inodes)
    process4 = multiprocessing.Process(target=hash_analizer) 

    process1.start()
    process2.start()
    process3.start()
    process4.start()
