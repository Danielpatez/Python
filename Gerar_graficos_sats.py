# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 11:46:31 2022

@author: danie

fazer graficos dos satelites juntos - identificar janelas de horarios juntos (quantidade de satelites mesmo periodo)
"""

import pandas as pd
import matplotlib.pyplot as plt

sat='G31'
valor=1


df=pd.read_csv('C:/Users/danie/Documents/PET/PESQUISA_02/2 - Leitura skyplot/LBHT/LBHT_2014_02_26_2014_02_27_23h_4h.txt')
df.rename(columns={' azim': 'azim', ' elev':'elev', ' value': 'value', ' time_utc': 'time_utc', ' station_id':'station_id'}, inplace=True)
df['time_utc']=pd.to_datetime(df['time_utc'])
df1=df
df1=df1.set_index('svid')

graf=df1[(df1.value >valor)].loc[sat]

plt.rcParams['xtick.labelsize'] = 30
plt.rcParams['ytick.labelsize'] = 30
fig = plt.figure(figsize=(30,20))
eixo = fig.add_axes([0, 0, 1, 1])
eixo.set_title('Indice S4', fontsize=40)
eixo.set_ylabel('S4', fontsize=40)
eixo.set_xlabel('Data/hora', fontsize=40)
eixo.plot(graf['time_utc'],graf['value'])
eixo.scatter(graf['time_utc'],graf['value'])