# ----------------------------------------------------------------------------
# Nome do Arquivo: sistemas_de_tempo.py
# Autor: Daniel Climaco Patêz
# Descrição: Este programa converte o tempo UTC para os seguintes sistemas:
# UT1 - TAI - GPS - TT - TDT - JD - MJD - TCG
# Data de Criação: 17 de Agosto de 2023
# ----------------------------------------------------------------------------

import math
#CONSTANTES
Lg = 6.969290134*10**(-10); 
Lb = 1.55051976772*10**(-8);
P0 = 6.55*10**(-5);
DUT1 =  -0.5;
leapseconds = 18;

#ENTRADA DE DADOS EM UTC
Y = 2023;   #ANO
M = 1;      #MES
D = 26;     #DIA
Hr = 2;     #HORA
Min = 54;   #MINUTOS
Sec = 0;    #SEGUNDOS

#---------------------------------------------

#CALCULOS

#FUNCAO SEMANA E SEGUNDOS GPS
def localtogps(timestring,timeformat,leapseconds,localoffset=0):
    import datetime
    epoch = datetime.datetime.strptime("1980-01-07 00:00:00","%Y-%m-%d %H:%M:%S")
    local = datetime.datetime.strptime(timestring,timeformat)
    utc = local - datetime.timedelta(hours=localoffset)
    diff = utc-epoch
    gpsWeek = diff.days/7
    secondsThroughDay = (utc.hour * 3600) + (utc.minute * 60) + utc.second
    if utc.isoweekday()== 7:
        weekday = 0
    else:
        weekday = utc.isoweekday()
    gpsSeconds = (weekday * 86400) + secondsThroughDay - leapseconds
    return (gpsWeek,gpsSeconds)

#FUNCAO CONVERSAO DATA GREGORIANA PARA DATA JULIANA
def date_to_jd(year,month,day):
    """
    Convert a date to Julian Day.
    
    Algorithm from 'Practical Astronomy with your Calculator or Spreadsheet', 
        4th ed., Duffet-Smith and Zwart, 2011.
    
    Parameters
    ----------
    year : int
        Year as integer. Years preceding 1 A.D. should be 0 or negative.
        The year before 1 A.D. is 0, 10 B.C. is year -9.
        
    month : int
        Month as integer, Jan = 1, Feb. = 2, etc.
    
    day : float
        Day, may contain fractional part.
    
    Returns
    -------
    jd : float
        Julian Day
        
    Examples
    --------
    Convert 6 a.m., February 17, 1985 to Julian Day
    
    >>> date_to_jd(1985,2,17.25)
    2446113.75
    
    """
    if month == 1 or month == 2:
        yearp = year - 1
        monthp = month + 12
    else:
        yearp = year
        monthp = month
    
    # this checks where we are in relation to October 15, 1582, the beginning
    # of the Gregorian calendar.
    if ((year < 1582) or
        (year == 1582 and month < 10) or
        (year == 1582 and month == 10 and day < 15)):
        # before start of Gregorian calendar
        B = 0
    else:
        # after start of Gregorian calendar
        A = math.trunc(yearp / 100.)
        B = 2 - A + math.trunc(A / 4.)
        
    if yearp < 0:
        C = math.trunc((365.25 * yearp) - 0.75)
    else:
        C = math.trunc(365.25 * yearp)
        
    D = math.trunc(30.6001 * (monthp + 1))
    
    jd = B + C + D + day + 1720994.5
    
    return jd

#HORAS DO DIA PARA SEGUNDOS DO DIA
Hs = Hr*3600 + Min*60 + Sec;
#UTC
UTC =  Hs;

#UT1
UT1 = UTC + DUT1;

#TAI
TAI = UTC + 37;

#GPS
GPS = TAI - 19;

local =f"{Y}-{M}-{D} {Hr}:{Min}:{Sec}"
formato = "%Y-%m-%d %H:%M:%S";
gpsweek,gpssec = localtogps(local, formato, leapseconds, localoffset=0);

#TEMPO TERRESTRE
TT = TDT = TAI + 32.184;

#DATA JULIANA
JD = date_to_jd(Y,M,D) + Hs/86400;

#DATA JULIANA MODIFICADA
MJD = JD - 2400000.5;

#TEMPO COORDENADA GEOCENTRICO
TCG = TT + Lg * (MJD - 43144.0)*86400;

#APRESENTACAO DAS CONVERSOES
MINUTO, SECS = divmod(UTC, 60) 
HORA, MINUTO = divmod(MINUTO, 60) 
print("UTC: {}/{}/{} at {:.0f}h {:.0f}min {:.2f}s\n".format(D,M,Y,HORA,MINUTO,SECS));

MINUTO, SECS = divmod(UT1, 60) 
HORA, MINUTO = divmod(MINUTO, 60) 
print("UT1: {}/{}/{} at {:.0f}h {:.0f}min {:.2f}s\n".format(D,M,Y,HORA,MINUTO,SECS));

MINUTO, SECS = divmod(TAI, 60) 
HORA, MINUTO = divmod(MINUTO, 60) 
print("TAI: {}/{}/{} at {:.0f}h {:.0f}min {:.2f}s\n".format(D,M,Y,HORA,MINUTO,SECS));

MINUTO, SECS = divmod(GPS, 60) 
HORA, MINUTO = divmod(MINUTO, 60) 
print("GPS: {}/{}/{} at {:.0f}h {:.0f}min {:.2f}s / {}s da semana GPS {}\n".format(D,M,Y,HORA,MINUTO,SECS,gpssec,math.floor(gpsweek)));

MINUTO, SECS = divmod(TT, 60) 
HORA, MINUTO = divmod(MINUTO, 60) 
print("TT ou TDT: {}/{}/{} at {:.0f}h {:.0f}min {:.3f}s\n".format(D,M,Y,HORA,MINUTO,SECS));

print("JD: {} dias \n".format(JD));

print("MJD: {} dias \n".format(MJD));

MINUTO, SECS = divmod(TCG, 60) 
HORA, MINUTO = divmod(MINUTO, 60) 
print("TCG: {}/{}/{} at {:.0f}h {:.0f}min {:.3f}s\n".format(D,M,Y,HORA,MINUTO,SECS));



#----------------------------------------
#OUTRAS RELACOES
#TCG - TT = Lg * (MJD - 43144.0)*86400;
#TCB - TDB = Lb * (MJD - 43144.0)*86400 + P0
#DTU1 = UT1 - UTC
#----------------------------------------

                 

