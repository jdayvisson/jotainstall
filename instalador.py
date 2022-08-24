#!/usr/bin/env python
import os, sys, subprocess

print("""\n


           ██  ██████  ████████  █████      ██ ███    ██ ███████ ████████  █████  ██      ██      
           ██ ██    ██    ██    ██   ██     ██ ████   ██ ██         ██    ██   ██ ██      ██      
           ██ ██    ██    ██    ███████     ██ ██ ██  ██ ███████    ██    ███████ ██      ██      
      ██   ██ ██    ██    ██    ██   ██     ██ ██  ██ ██      ██    ██    ██   ██ ██      ██      
       █████   ██████     ██    ██   ██     ██ ██   ████ ███████    ██    ██   ██ ███████ ███████ 
                                                                                            
                                                                                            

                                                                               
                    Aplicação criada para pesquisas, utilizando dorks do google
                                         Criado por @JOTA 

                      Exclusivo para a turma do curso de Hacker Investigador!

                                          Version : 1.0
                                    Codename: Jota Instalador
                                                                                     """)

l = '1'
o = '2'


print("")
print("""###########################################    LISTA    ###########################################\n\n""")

print('Linset: (1) | Osintgram: (2)')

print('\n')
query = int(input('Digite um número da lista: '))
print("")
print('\n')
print("")

if query == 1:
	print(l)	
else: 
	print('Valor invalido...\n')

	query = int(input('Digite novamente um número da lista: '))
	print("")

	if query == 1:
		print(l)	
	else: 
		print('Que pena, tente novamente outra hora ;)\n')

	
		if query == 2:
			print(o)	
		else: 
			print('Valor invalido...\n')

		query = int(input('Digite novamente um número da lista: '))
		print("")
	
		if query == 2:
			print(o)	
		else: 
			print('Que pena, tente novamente outra hora ;)\n')

	sys.exit()

l = 'git clone https://github.com/creadpag/linset.git; sudo apt update; sudo apt-get install isc-dhcp-server; sudo apt-get install hostapd; sudo apt-			get install lighttpd; sudo apt-get -y install mdk3; sudo apt-get install Php8.1-cgi; git clone https://github.com/hacker3983/pyrit-installer && cd pyrit-installer && sudo bash install.sh; cd linset/; ls; sudo ./linset'

o = 'git clone https://github.com/Datalux/Osintgram.git'


	
os.system(l)
os.system(o)







