# -*- coding: utf-8 -*-
"""
Created on Mar 2021

@author: danielPatez
"""

import math
import statistics
import csv
import time
sdn=[]
sde=[]
sdu=[]
triade=[]
chave=0
chave2=0
chave_M=1
"""
Utilize este espaco para substituição das variaveis
statistics_57
gval0570
mgbh0570
mgin0570
mgmc0570
mgub0570
mgva0570
vico0570
"""
def leitura (arq, name):
    finp=open(arq,'r')
    cont=0
    linhas=0
    
    global chave, chave2,chave_M
    for line in finp:
        cont+=1
        dn=de=du=0
        if cont>18:
               
            ls=line.split(' ')
            n=len(ls)
            coluna=0
            for a in range(0,(n)):

                #contvet+=1
                if ls[a]!='':
                    coluna+=1

                                               
                    if coluna==2:
                        time=ls[a]
                        if chave_M==1 and ((time[0:2])=='21'or (time[0:2])=='22' or (time[0:2])=='23'):
                            chave=1
                            chave2=1
                        else:
                            chave=0
                        
                
                        if chave2==1:
                            if ((time[0:2])=='00' or (time[0:2])=='01' or (time[0:2])=='02' or (time[0:2])=='03' or (time[0:2])=='04' or (time[0:2])=='05' or (time[0:2])=='06' or (time[0:2])=='07' or (time[0:2])=='08'):
                                chave=1
                            if (time[0:2])=='09':
                                chave=0
                                chave_M=0
                            
                        
                    if coluna==8:
                        if chave==1:
                            linhas+=1
                            sdn.append(float(ls[a]))
                            dn=float(ls[a])
                    
                    if coluna==9:
                        if chave==1:                        
                            sde.append(float(ls[a]))
                            de=float(ls[a])
                        
                    if coluna==10:
                        if chave==1:
                            sdu.append(float(ls[a]))
                            du=float(ls[a])
                            tri=(dn**2 + de**2 + du**2)**0.5
                            triade.append(tri)
    
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
    somaquad_triade=0
    somaquad_sdn=0
    somaquad_sde=0
    somaquad_sdu=0
    
    n=cont-19
    
    for c in range(0,linhas):
                
        somaquad_triade= somaquad_triade + triade[(ident)]
        somaquad_sdn= somaquad_sdn + sdn[(ident)]**2
        somaquad_sde= somaquad_sde + sde[(ident)]**2
        somaquad_sdu= somaquad_sdu + sdu[(ident)]**2
        ident+=1
    rmse_triade = math.sqrt(somaquad_triade/linhas)
    rmse_sdn = math.sqrt(somaquad_sdn/linhas)
    rmse_sde = math.sqrt(somaquad_sde/linhas)
    rmse_sdu = math.sqrt(somaquad_sdu/linhas)
    
    with open('statistics_57.csv', 'a', newline='') as file:
       writer = csv.writer(file)
       writer.writerow([name,desvpad_sdn, rmse_sdn, desvpad_sde, rmse_sde, desvpad_sdu, rmse_sdu, media_sdn, media_sde, media_sdu, maior_sdn, maior_sde, maior_sdu, menor_sdn, menor_sde, menor_sdu, rmse_triade])

    #Estacao 2
    sdn.clear()
    sde.clear()
    sdu.clear()
print("Processando...")
with open('statistics_57.csv', 'w+', newline='') as file:
   writer = csv.writer(file)
   writer.writerow(["Estacao","desvpad_sdn", "rmse_sdn", "desvpad_sde","rmse_sde", "desvpad_sdu", "rmse_sdu", "media_sdn", "media_sde", "media_sdu", "max_sdn", "max_sde", "max_sdu", "min_sdn", "min_sde", "min_sdu", "rmse_triade"])

#Arquivos .pos a serem lidos (Informe caminho ou mantenha os arquivos na mesma pasta)
arq=  'gval0570.pos'
name= 'gval0570'
leitura(arq,name)
  
arq=  'mgbh0570.pos'
name= 'mgbh0570'
leitura(arq,name)

arq=  'mgin0570.pos'
name= 'mgin0570'
leitura(arq,name)

arq=  'mgmc0570.pos'
name= 'mgmc0570'
leitura(arq,name)

arq=  'mgub0570.pos'
name= 'mgub0570'
leitura(arq,name)

arq=  'mgva0570.pos'
name= 'mgva0570'
leitura(arq,name)

arq=  'vico0570.pos'
name= 'vico0570'
leitura(arq,name)

print("\n...\n\nProcesso Concluido com sucesso.")
time.sleep(4)    # pause 4 seconds
SystemExit()
       
