# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 01:05:40 2022

@author: danie
"""
import pandas as pd

#Abre o arquivo de relatorio do ISMR a ser lido
df1=pd.read_csv('C:/Users/danie/Documents/PET/PESQUISA_02/2 - Leitura skyplot/LBHT/LBHT_2014_02_26_2014_02_27_23h_4h.txt')


#Formata a hora para o padrao aceito no teqc
columns= df1.filter(like=' time_utc')
for column in columns:
    df1[column]= df1[column].str.replace('-','_').str.replace(' ','_').str.slice(1)
   
    
#Definindo variaveis para analise
num_max_s4= 1
svid_acima= []
value= []
time_utc= []

svid_free=[]
value_free= []
time_utc_free= []


#Laco para pegar observacoes de S4 acima de "num_max_s4" bem como abaixo deste valor
for a in df1.index:
    if df1[' value'][a] > num_max_s4:       
        svid_acima.append(df1['svid'][a])
        value.append(df1[' value'][a])
        time_utc.append(df1[' time_utc'][a])
        
        
    else:
        svid_free.append(df1['svid'][a])
        value_free.append(df1[' value'][a])
        time_utc_free.append(df1[' time_utc'][a])


#Criando DataFrame com lista das observacoes com S4 acima de "num_max_s4"         
df2=pd.DataFrame(list(zip(svid_acima, value, time_utc)), columns= ['SVID', 'VALUE', 'TIME_UTC'] )
df3=pd.DataFrame(list(zip(svid_free, value_free, time_utc_free)), columns= ['SVID_free', 'VALUE_free', 'TIME_UTC_free'] )

df2.to_csv('C:/Users/danie/Documents/PET/PESQUISA_02/2 - Leitura skyplot/LBHT/s4_maior_1.csv', index=False)
df2.to_csv('C:/Users/danie/Documents/PET/PESQUISA_02/2 - Leitura skyplot/LBHT/s4_maior_1_obs.csv', index=False)


#Passando lista de svids a cortar e forcar
svid_unique= pd.unique(df2["SVID"])
txt_svid_acima= ','.join(svid_unique)

svid_unique_free= pd.unique(df3["SVID_free"])
txt_svid_free= ','.join(svid_unique_free)

#Satelites que não tiveram s4 acima
sat_free = [item for item in svid_unique_free if item not in svid_unique]
txt_sat_free= ','.join(sat_free)

with open(r"C:/Users/danie/Documents/PET/PESQUISA_02/2 - Leitura skyplot/LBHT/s4_maior_1_obs.csv", "r") as file:
    data = file.read()
    data = data.replace(",","	")

with open(r"C:/Users/danie/Documents/PET/PESQUISA_02/2 - Leitura skyplot/LBHT/s4_maior_1_obs.csv", "w") as file:
    file.write(data + "\n \n" + "Satelites a cortar: " + "\n"+ txt_svid_acima + "\n \n" + "Satelites a forcar: " + "\n" + txt_sat_free)
    

"""
#Escrevendo ao fim do arquivo as info
arq= open('C:/Users/danie/Documents/PET/PESQUISA_02/2 - Leitura skyplot/LBHT/s4_maior_1_obs.csv', 'a')
arq.write("\n \n" + "Satelites a cortar: " + "\n"+ txt_svid_acima + "\n \n" + "Satelites a forcar: " + "\n" + txt_sat_free)
arq.close()
"""
