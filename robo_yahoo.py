from datetime import datetime
from json import loads
from urllib.request import urlopen
import time, sys

def yahoo():
    #request = urlopen('https://query1.finance.yahoo.com/v8/finance/chart/PETR4.SA').read() #Petr4
    request = urlopen('https://query1.finance.yahoo.com/v8/finance/chart/USDBRL=X').read()
    price = loads(request)['chart']['result'][0]['meta']
    valor = price['regularMarketPrice']
    
    dt = int(price['regularMarketTime'])
    datayahoo = datetime.fromtimestamp(dt).strftime('%d/%m/%Y às %H:%M:%S') # era .utcfromtimestamp no lugar do fromtimestamp
       
    if __name__ == '__main__':
       # .4f o resultado é em milessimo .3f centesimo .2f ou 1.f
       print('Dolar Comercial em : ' + format(valor, '.4f') + ' em ' + datayahoo) 
       
	   #print('Valor da Petr4"datayahoo": {regularMarketPrice}'.format(**price))      
	   #print('Dolar Comercial em : {regularMarketPrice}'.format(**price) + ' em ' + datayahoo)
       
	   #print(datetime.utcfromtimestamp(ts2).strftime('%d/%m/%Y às %H:%M:%S'))

def executar_yahoo():
    yahoo()  
    for i in range(0, 14):
        time.sleep(12)
        yahoo()
       
executar_yahoo()        