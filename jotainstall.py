#!/usr/bin/env python3

import os, sys, time

clear

print("""\n
		   _       _          _           _        _ _ 
		  (_) ___ | |_ __ _  (_)_ __  ___| |_ __ _| | |
		  | |/ _ \| __/ _` | | | '_ \/ __| __/ _` | | |
		  | | (_) | || (_| | | | | | \__ \ || (_| | | |
		 _/ |\___/ \__\__,_| |_|_| |_|___/\__\__,_|_|_|
		|__/                                           

	    Aplicação criada para facilitar a instalação de scripts
			        Criado por @JOTA
			         
   Uma pequena contribuição para ajudar turma do curso de Hacker Investigador!
   
\033[1;91m                                 Version : 1.0\033[0;0m 
			   Codename: Jota Instalador
			   
			   
                                                                                     """)
                                                                                     

#VARIAVEIS PARA LIMPAR E RETORNAR AO MENU +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

limpar = 'clear'
iniciar = 'python jotainstall.py'
sair = 'cd ~'

#FIM+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#VARIÁVEIS DOS PROGRAMAS QUE VÃO SER INSTALADOS +++++++++++++++++++++++++++++++++++++++++++++++++++++++++


exiftool = 'sudo apt update; sudo apt install libimage-exiftool-perl; git clone https://github.com/exiftool/exiftool.git; cd exiftool' #sudo cp -rf * /usr/bin; cd ..; sudo rm -r exiftool'

osintgram = 'git clone https://github.com/Datalux/Osintgram; sudo apt update; sudo apt-get install crackmapexec; cd Osintgram; sudo pip3 install -r requirements.txt; cd config; nano credentials.ini; cd ..' #sudo cp -rf * /usr/bin; cd ..; sudo rm -r Osintgram'

nphisher = 'sudo apt update; sudo tar xvzf ~/Downloads/ngrok-v3-stable-linux-amd64.tgz -C /usr/local/bin; git clone https://github.com/rdxlr/NPhisher; cd NPhisher' #sudo cp -rf * /usr/bin; cd ..; sudo rm -r NPhisher'

sherlock = 'sudo apt update; git clone https://github.com/sherlock-project/sherlock.git; cd sherlock; python3 -m pip install -r requirements.txt; cd sherlock' #sudo cp -rf * /usr/bin; cd ..; cd ..; sudo rm -r sherlock'

spiderfoot = 'sudo apt update; git clone https://github.com/smicallef/spiderfoot.git; cd spiderfoot; sudo pip install -r requirements.txt; wget https://github.com/smicallef/spiderfoot/archive/v3.5.tar.gz; tar zxvf v3.5.tar.gz; cd spiderfoot-3.5; sudo pip install -r requirements.txt; cd ..' #sudo cp -rf * /usr/bin; cd ..; sudo rm -r spiderfoot'

seeker = 'sudo apt update; sudo git clone https://github.com/thewhiteh4t/seeker; cd seeker; sudo chmod 777 install.sh; sudo ./install.sh' #sudo python seeker'

#FIM ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#MENU DE OPÇÕES +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def menu_principal():
    
    print('\033[;1m- - ---MENU DE OPÇÕES--- - -')
    print('''
       
    \033[1;33m   [1] EXIFTOOL
    \033[;001m   [2] OSINTGRAM
    \033[1;33m   [3] NPHISHER
    \033[;001m   [4] SHERLOCK
    \033[1;33m   [5] SPIDERFOOT
    \033[;001m   [6] SEEKER
    
    \033[1;92m   [0] SAIR\033[0;0m
        
    
    ''')	
menu_principal()

#FIM+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#LAÇO DE REPETIÇÃO CASO A OPÇÃO SEJA INVÁLIDA +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

consulta = int(input('\033[;1m Escolha a opção desejada: '))
while consulta < 0 or consulta > 7:
    consulta = int(input('\n Opção inválida. Por favor, selecione uma das opções do menu: '))

#FIM ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# CONDIÇÕES +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  
else:
	if consulta == 1:
		ferr = os.system(exiftool)
		print(exiftool)
		limpe = os.system(limpar)
		print('\n \n \n ### Instalação Concluída! ###')
		time.sleep(3)
		lim = os.system(limpar)
		menu = os.system(iniciar)
		
	if consulta == 2:
		ferr = os.system(osintgram)
		limpe = os.system(limpar)
		print('\n \n \n ### Instalação Concluída! ###')
		time.sleep(3)
		lim = os.system(limpar)
		menu = os.system(iniciar)
	
	if consulta == 3:
		ferr = os.system(nphisher)
		limpe = os.system(limpar)
		print('\n \n \n ### Instalação Concluída! ###')
		time.sleep(3)
		lim = os.system(limpar)
		menu = os.system(iniciar)
		
	if consulta == 4:
		ferr = os.system(sherlock)
		lim = os.system(limpar)
		print('\n \n \n ### Instalação Concluída! ###')
		time.sleep(3)
		limpe = os.system(limpar)
		menu = os.system(iniciar)
		
	if consulta == 5:
		ferr = os.system(spiderfoot)		
		lim = os.system(limpar)
		print('\n \n \n ### Instalação Concluída! ###')
		time.sleep(3)
		limpe = os.system(limpar)
		menu = os.system(iniciar)
	
	if consulta == 6:
		ferr = os.system(seeker)		
		lim = os.system(limpar)
		print('\n \n \n ### Instalação Concluída! ###')
		time.sleep(3)
		limpe = os.system(limpar)
		menu = os.system(iniciar)
			
	if consulta == 7:
		ferr = os.system(sair)
		print(f'\n ****** Opa! Valeu e volte sempre ;) ******')
		time.sleep(3)
		
		
#FIM ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        


    


   

