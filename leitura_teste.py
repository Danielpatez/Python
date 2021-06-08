# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:19:58 2021

@author: danielPatez
"""

import math
import statistics
import csv
import time
sdn=[]
sde=[]
sdu=[]
"""
Utilize este espação para substituição das variaveis
statistics_26
gval0260
mgbh0260
mgin0260
mgmc0260
mgub0260
mgva0260
vico0260
"""
def leitura (arq, name):
    finp=open(arq,'r')
    cont=0
    for line in finp:
        cont+=1
        if cont>18:
               
            ls=line.split(' ')
            n=len(ls)
            #print('tamanho linha:', n)
            #print(ls)
            #print('\n')
            #print(ls[1])
            #contvet=-1
            coluna=0
            for a in range(0,(n)):
                #contvet+=1
                if ls[a]!='':
                    coluna+=1
                    #print(coluna)
                    #print(contvet)
                    #print(a)
                    #print(ls[a])
                    if coluna==8:
                        sdn.append(float(ls[(a)]))
                        #print("sdn: ", ls[a])
                    if coluna==9:
                        sde.append(float(ls[a]))
                    if coluna==10:
                        sdu.append(float(ls[a]))
                #if ls>14:
                 #   if ls[coluna]!=' '
                  #  n_sdn=n
                    #sdn.append(float(ls[(coluna)]))
 #calculo desvio padrao
    desvpad_sdn = statistics.stdev(sdn)
    desvpad_sde = statistics.stdev(sde)
    desvpad_sdu = statistics.stdev(sdu)
    #calculo media
    media_sdn = statistics.mean(sdn)
    media_sde = statistics.mean(sde)
    media_sdu = statistics.mean(sdu)
    #calculo maximo
    maior_sdn = max(sdn)
    maior_sde = max(sde)
    maior_sdu = max(sdu)
    #calculo minimo
    menor_sdn = min(sdn)
    menor_sde = min(sde)
    menor_sdu = min(sdu)
    #calculo rmse
    ident=0
    somaquad_sdn=0
    somaquad_sde=0
    somaquad_sdu=0
    n=cont-19
    for c in range(0,(cont-18)):
        #print(ident)
        #print(cont)
        somaquad_sdn= somaquad_sdn + sdn[(ident)]**2
        somaquad_sde= somaquad_sde + sde[(ident)]**2
        somaquad_sdu= somaquad_sdu + sdu[(ident)]**2
        ident+=1
    rmse_sdn = math.sqrt(somaquad_sdn/n)
    rmse_sde = math.sqrt(somaquad_sde/n)
    rmse_sdu = math.sqrt(somaquad_sdu/n)
    
    with open('statistics_26.csv', 'a', newline='') as file:
       writer = csv.writer(file)
       #writer.writerow(["Estacao", "desvpad_sdn", "rmse_sdn", "desvpad_sde","rmse_sde", "desvpad_sdu","rmse_sdu"])
       writer.writerow([name,desvpad_sdn, rmse_sdn, desvpad_sde, rmse_sde, desvpad_sdu, rmse_sdu, media_sdn, media_sde, media_sdu, maior_sdn, maior_sde, maior_sdu, menor_sdn, menor_sde, menor_sdu])

    #Estacao 2
    sdn.clear()
    sde.clear()
    sdu.clear()
print("Processando...")
with open('statistics_26.csv', 'w+', newline='') as file:
   writer = csv.writer(file)
   writer.writerow(["Estacao","desvpad_sdn", "rmse_sdn", "desvpad_sde","rmse_sde", "desvpad_sdu", "rmse_sdu", "media_sdn", "media_sde", "media_sdu", "max_sdn", "max_sde", "max_sdu", "min_sdn", "min_sde", "min_sdu"])

arq=  'gval0260.pos'
name= 'gval0260'
leitura(arq,name)

arq=  'mgbh0260.pos'
name= 'mgbh0260'
leitura(arq,name)

arq=  'mgin0260.pos'
name= 'mgin0260'
leitura(arq,name)

arq=  'mgmc0260.pos'
name= 'mgmc0260'
leitura(arq,name)

arq=  'mgub0260.pos'
name= 'mgub0260'
leitura(arq,name)

arq=  'mgva0260.pos'
name= 'mgva0260'
leitura(arq,name)

arq=  'vico0260.pos'
name= 'vico0260'
leitura(arq,name)

print("\n...\n\nProcesso Concluido com sucesso.")
time.sleep(4)    # pause 5.5 seconds
SystemExit()
       