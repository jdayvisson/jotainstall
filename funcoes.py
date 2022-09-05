#!/usr/bin/env python

import os, sys

#LISTA DOS PROGRAMAS QUE VÃO SER INSTALADOS

limpar = 'clear'
iniciar = 'python funcoes.py'

linset = 'git clone https://github.com/creadpag/linset.git; sudo apt update; sudo apt-get install isc-dhcp-server; sudo apt-get install hostapd; sudo apt-get install lighttpd; sudo apt-get -y install mdk3; sudo apt-get install Php8.1-cgi; git clone https://github.com/hacker3983/pyrit-installer && cd pyrit-installer && sudo bash install.sh'

osintgram = 'git clone https://github.com/Datalux/Osintgram.git'
 
atualizacao = 'sudo apt update'



#MENU DE OPÇÕES

def menu_principal():
    print('\n')
    print('----------MENU PRINCIPAL----------')
    print('')
    print('')
    print('\033[1;33m [1] LINSET')   #TEXTO AMARELO
    print('\033[;1m [2] OSINTGRAM')  #TEXTO BRANCO
    print('\033[1;33m [3] UPDATE')   #TEXTO AMARELO	
    print('\n')
menu_principal()


#LAÇO DE REPETIÇÃO CASO A OPÇÃO SEJA INVÁLIDA

consulta = int(input('\033[;1m Escolha a opção desejada: '))
while consulta < 0 or consulta > 3:
    print('Opção inválida. Por favor, selecione uma das opções do menu.')
    consulta = int(input('Escolha a função desejada: '))

    
else:
	if consulta == 1:
		fun = os.system(linset)
		print(linset)
		lim = os.system(limpar)
		home = os.system(iniciar)
		

	if consulta == 2:
		fun = os.system(osintgram)
		print(osintgram)
		lim = os.system(limpar)
		home = os.system(iniciar)
	
	if consulta == 3:
		fun = os.system(atualizacao)
		print(atualizacao)
		lim = os.system(limpar)
		home = os.system(iniciar)
		
        


    


   

