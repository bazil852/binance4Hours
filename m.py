import os

from binance.client import Client

from PIL import Image, ImageEnhance
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
import telegram
from PIL import ImageFont
from PIL import ImageDraw 
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import time
from dateutil import parser
import math
import os.path
import time
import plotly.graph_objects as go
from datetime import datetime
import mplfinance as mpf
import os
from datetime import date

start_time = time.time()

if not os.path.exists("images"):
    os.mkdir("images")


TELEGRAM_BOT_TOKEN = '2012524709:AAH9G21vDNTZyrGxTTbFpx2m-PwHBY_fmsU'
TELEGRAM_CHAT_ID = '-589824218'
PHOTO_PATH = 'Result.png'
PHOTO_PATH1 = 'Result1.png'
PHOTO_PATH2 = 'Result2.png'
PHOTO_PATH3 = 'Result3.png'


binance_api_key = '7wLSiwoaXXU57j5fhWLNA6dbGTlvqommHrmPm36xhwyfSo2wFYBYztJqx6aR9hmB'
binance_api_secret = 'srjlGJtOB4z8pzrZudJmhvjRxBaLdtK30Ou1CHOG0S0XpFHYKuCznZXp9CXLcdbn'

binsizes = { "4h": 60}
batch_size = 4

names=['BTCUSDT','BTCUSDT','BTCUSDT','BTCUSDT','BTCUSDT','BTCUSDT','BTCUSDT','ADAUSDT','AIONUSDT','ALGOUSDT','ALICEUSDT','ALPACAUSDT','ALPHAUSDT','ANKRUSDT','ARDRUSDT','ARUSDT','ATAUSDT','ATOMUSDT','AVAUSDT','AVAXUSDT','BTCUSDT','BANDUSDT','BATUSDT','BCHUSDT','BLZUSDT','BTTUSDT','BURGERUSDT','CHRUSDT','CHZUSDT','CKBUSDT','COCOSUSDT','COSUSDT','COTIUSDT','CRVUSDT','CTKUSDT','CTSIUSDT','CTXCUSDT','CVCUSDT','TCTUSDT','DASHUSDT','DATAUSDT','DCRUSDT','DEGOUSDT','DENTUSDT','DGBUSDT','DNTUSDT','DOGEUSDT','DOTUSDT','DREPUSDT']
names1=['BTCUSDT','BTCUSDT','BTCUSDT','BTCUSDT','BTCUSDT','BTCUSDT','BTCUSDT','DUSKUSDT','EGLDUSDT','ENJUSDT','EOSUSDT','ETCUSDT','ELFUSDT','FETUSDT','FILUSDT','FIROUSDT','FLMUSDT','FLOWUSDT','FTMUSDT','FTTUSDT','GRTUSDT','GTOUSDT','GALAUSDT','HBARUSDT','HIVEUSDT' ,'HNTUSDT' , 'HOTUSDT' , 'ICPUSDT' , 'ICXUSDT' , 'IOSTUSDT' , 'IOTAUSDT' , 'IOTXUSDT' , 'IRISUSDT' , 'JUVUSDT' , 'KEEPUSDT' , 'KEYUSDT' , 'KLAYUSDT' , 'KMDUSDT' , 'KSMUSDT' , 'LINAUSDT' , 'LITUSDT' , 'LRCUSDT' , 'LSKUSDT' , 'LTCUSDT' , 'LTOUSDT' , 'LUNAUSDT', 'MANAUSDT' , 'MASKUSDT' , 'MATICUSDT']
names2=['BTCUSDT','BTCUSDT','BTCUSDT','BTCUSDT','BTCUSDT','BTCUSDT','BTCUSDT','ZENUSDT' , 'XECUSDT' , 'XRPUSDT' , 'XTZUSDT' , 'XLMUSDT' , 'XVGUSDT' , 'ZECUSDT','ZENUSDT','ZRXUSDT','ZILUSDT', 'STORJUSDT' , 'STPTUSDT' , 'STRAXUSDT' , 'STXUSDT' , 'SYSUSDT' , 'SOLUSDT' , 'SFPUSDT' , 'SKLUSDT' , 'SLPUSDT' , 'SXPUSDT' , 'SCUSDT' , 'SNXUSDT' , 'TWTUSDT' , 'TRBUSDT' , 'TRXUSDT' , 'TFUELUSDT' , 'TKOUSDT' , 'TLMUSDT' , 'TCTUSDT' , 'TVKUSDT' , 'UTKUSDT' , 'UNFIUSDT' , 'VETUSDT' , 'VTHOUSDT' , 'VITEUSDT' , 'VIDTUSDT' , 'WRXUSDT' , 'WTCUSDT' , 'WINGUSDT' , 'WANUSDT' , 'WAVESUSDT' , 'WAXPUSDT']
names3=['WNXMUSDT', 'MINAUSDT' , 'MITHUSDT' , 'MBOXUSDT' , 'NBSUSDT' , 'NEARUSDT' , 'NULSUSDT' , 'NKNUSDT' , 'OCEANUSDT' , 'OGNUSDT' , 'OMGUSDT' , 'OMUSDT' , 'ONEUSDT' , 'ONGUSDT' , 'ONTUSDT' , 'OXTUSDT' , 'PAXGUSDT' , 'PHAUSDT' , 'PNTUSDT' , 'POLSUSDT' , 'PONDUSDT' , 'PSGUSDT' , 'PUNDIXUSDT' , 'POLYUSDT' , 'PROMBUSD' , 'QNTUSDT' , 'QTUMUSDT' , 'QUICKUSDT' , 'RIFUSDT' , 'RLCUSDT' , 'ROSEUSDT' , 'RSRUSDT' , 'RVNUSDT' , 'SANDUSDT' , 'STMXUSDT','MBLUSDT' , 'MDTUSDT' ]


def binanceklines(symbol,interval='4h',limit=4,since="1 day ago UTC"):
    klines = bina.futures_klines(symbol=symbol,interval={'4h':Client.KLINE_INTERVAL_4HOUR,'4h':Client.KLINE_INTERVAL_4HOUR}['4h'],since="1 day ago UTC",limit=4)
    data = pd.DataFrame(klines, columns = ['ts', 'o', 'h', 'l', 'c', 'v', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore' ])
    data=data.apply(pd.to_numeric)
    data['ts'] = pd.to_datetime(data['ts'], unit='ms')
    data=data.set_index('ts')
    return data

bina = Client('','')
count=0
for i in range (len(names)):

    print(count+1,' Fetching: ',names[i])

    klines = bina.get_historical_klines(names[i], Client.KLINE_INTERVAL_4HOUR,"1 day ago UTC",limit=4)
    data = pd.DataFrame(klines, columns = ['ts', 'o', 'h', 'l', 'c', 'v', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore' ])
    data=data.apply(pd.to_numeric)
    data['ts'] = pd.to_datetime(data['ts'], unit='ms')
    df=data

    fig = go.Figure(data=[go.Candlestick(x=df.index,open=df['o'],high=df['h'],low=df['l'],close=df['c'])])
    fig.update_layout(title="<b>"+names[i]+"</b>", font=dict(
        family="Courier New, bold",
        size=50
    ))
    #fig.show()
    #fig.savefig('img/2.PNG')
    
    fig.write_image(str("images/fig"+str(count)+".PNG"))
    count+=1




for i in range (len(names1)):

    print(count+1,'Fetching: ',names1[i])

    klines = bina.get_historical_klines(names1[i], Client.KLINE_INTERVAL_4HOUR,"1 day ago UTC",limit=4)
    data = pd.DataFrame(klines, columns = ['ts', 'o', 'h', 'l', 'c', 'v', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore' ])
    data=data.apply(pd.to_numeric)
    data['ts'] = pd.to_datetime(data['ts'], unit='ms')
    df=data

    fig = go.Figure(data=[go.Candlestick(x=df.index,open=df['o'],high=df['h'],low=df['l'],close=df['c'])])
    fig.update_layout(title="<b>"+names1[i]+"</b>", font=dict(
        family="Courier New, bold",
        size=50
    ))
    #fig.show()
    #fig.savefig('img/2.PNG')
    
    fig.write_image(str("images/fig"+str(count)+".PNG"))
    count+=1
    

for i in range (len(names2)):

    print(count+1,'Fetching: ',names2[i])

    klines = bina.get_historical_klines(names2[i], Client.KLINE_INTERVAL_4HOUR,"1 day ago UTC",limit=4)
    data = pd.DataFrame(klines, columns = ['ts', 'o', 'h', 'l', 'c', 'v', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore' ])
    data=data.apply(pd.to_numeric)
    data['ts'] = pd.to_datetime(data['ts'], unit='ms')
    df=data

    fig = go.Figure(data=[go.Candlestick(x=df.index,open=df['o'],high=df['h'],low=df['l'],close=df['c'])])
    fig.update_layout(title="<b>"+names2[i]+"</b>", font=dict(
        family="Courier New, bold",
        size=50
    ))
    #fig.show()
    #fig.savefig('img/2.PNG')
    
    fig.write_image(str("images/fig"+str(count)+".PNG"))
    count+=1
    

for i in range (len(names3)):

    print(count+1,'Fetching: ',names3[i])

    klines = bina.get_historical_klines(names3[i], Client.KLINE_INTERVAL_4HOUR,"1 day ago UTC",limit=4)
    data = pd.DataFrame(klines, columns = ['ts', 'o', 'h', 'l', 'c', 'v', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore' ])
    data=data.apply(pd.to_numeric)
    data['ts'] = pd.to_datetime(data['ts'], unit='ms')
    df=data

    fig = go.Figure(data=[go.Candlestick(x=df.index,open=df['o'],high=df['h'],low=df['l'],close=df['c'])])
    fig.update_layout(title="<b>"+names3[i]+"</b>", font=dict(
        family="Courier New, bold",
        size=50
    ))
    #fig.show()
    #fig.savefig('img/2.PNG')
    
    fig.write_image(str("images/fig"+str(count)+".PNG"))
    count+=1





'''
    plt.rcParams["figure.figsize"] = (10,8)
    fig, axlist=mpf.plot(df.apply(pd.to_numeric))
    fig.saveefig('img/2.PNG')

    print('Working')
'''


    
new = Image.new("RGBA", (7500,5000),color=(255,255,255,0))
new1 = Image.new("RGBA", (7500,5000),color=(255,255,255,0))
new2 = Image.new("RGBA", (7500,5000),color=(255,255,255,0))
new3 = Image.new("RGBA", (7500,5000),color=(255,255,255,0))

img=[]

c=0
x=0
y=100
count=0
for i in range(0,len(names)):
    if (((i)%7==0) and (i>0)):
        y+=700
        x=0
    img.insert(i,Image.open(str("images/fig"+str(count)+".PNG")))
    img[i] = img[i].resize((1000,700))
    width, height = img[i].size
    left = 0
    top = 0
    right = 1000
    bottom = 500
    
    img[i] = img[i].crop((left, top, right, bottom))
    img[i] = img[i].resize((1000,600))
    new.paste(img[i], (x,y))
    x+=1000
    print("Adding ",names[i], " to Result.")
    count+=1

draw = ImageDraw.Draw(new)
font = ImageFont.truetype("arial.ttf",85)
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
draw.text((2400, 5),dt_string,(255,255,255),font=font)

new.save("Result.png")



img=[]

c=0
x=0
y=100

for i in range(0,len(names1)):
    if (((i)%7==0) and (i>0)):
        y+=700
        x=0
    img.insert(i,Image.open(str("images/fig"+str(count)+".PNG")))
    img[i] = img[i].resize((1000,700))
    width, height = img[i].size
    left = 0
    top = 0
    right = 1000
    bottom = 500
    
    img[i] = img[i].crop((left, top, right, bottom))
    img[i] = img[i].resize((1000,600))
    new1.paste(img[i], (x,y))
    x+=1000
    print("Adding ",names1[i], " to Result.")
    count+=1

draw = ImageDraw.Draw(new1)
font = ImageFont.truetype("arial.ttf",85)
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
draw.text((2400, 5),dt_string,(255,255,255),font=font)

new1.save("Result1.png")




img=[]

c=0
x=0
y=100
for i in range(0,len(names2)):
    if (((i)%7==0) and (i>0)):
        y+=700
        x=0
    img.insert(i,Image.open(str("images/fig"+str(count)+".PNG")))
    img[i] = img[i].resize((1000,700))
    width, height = img[i].size
    left = 0
    top = 0
    right = 1000
    bottom = 500
    
    img[i] = img[i].crop((left, top, right, bottom))
    img[i] = img[i].resize((1000,600))
    new2.paste(img[i], (x,y))
    x+=1000
    print("Adding ",names2[i], " to Result.")
    count+=1

draw = ImageDraw.Draw(new2)
font = ImageFont.truetype("arial.ttf",85)
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
draw.text((2400, 5),dt_string,(255,255,255),font=font)

new2.save("Result2.png")



img=[]

c=0
x=0
y=100
for i in range(0,len(names3)):

    if (((i)%7==0) and (i>0)):
        y+=700
        x=0

    img.insert(i,Image.open(str("images/fig"+str(count)+".PNG")))
    img[i] = img[i].resize((1000,700))
    width, height = img[i].size
    left = 0
    top = 0
    right = 1000
    bottom = 500
    
    img[i] = img[i].crop((left, top, right, bottom))
    img[i] = img[i].resize((1000,600))
    new3.paste(img[i], (x,y))
    x+=1000
    #print("Adding ",names3[i], " to Result.")
    count+=1

draw = ImageDraw.Draw(new3)
font = ImageFont.truetype("arial.ttf",85)
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
draw.text((2400, 5),dt_string,(255,255,255),font=font)

new3.save("Result3.png")



bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="From Binance Bot")

bot.sendDocument(chat_id=TELEGRAM_CHAT_ID, document=open(PHOTO_PATH, 'rb'))

bot.sendDocument(chat_id=TELEGRAM_CHAT_ID, document=open(PHOTO_PATH1, 'rb'))

bot.sendDocument(chat_id=TELEGRAM_CHAT_ID, document=open(PHOTO_PATH2, 'rb'))

bot.sendDocument(chat_id=TELEGRAM_CHAT_ID, document=open(PHOTO_PATH3, 'rb'))


print("--- %s seconds ---" % (time.time() - start_time))