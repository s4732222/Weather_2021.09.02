import urllib.request
from bs4 import BeautifulSoup
import pandas as pd


adress=[]
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V016960")#漢口路(山西路~中清路間)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V440470")#德芳南路
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V028800")#經貿路
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V115901")#市政路-環中路橋外慢車道(往北)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V003401")#臺灣大道-黎明路(往北)


value=[]
#寫成i個陣列儲存
for i in range(len(adress)):
    data=[]
    html = urllib.request.urlopen(adress[i]).read()
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup)

#下載關鍵字
    table = soup.find('table', {'class': 'table table-bordered table-striped table-hover table-condensed'})
    trs = table.find_all('tr')[1:]
    rows = list()

#用逗號分隔
    for tr in trs:
        rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr('td')])
    print(rows)

#判斷網址有幾筆車流，取該車流出來
    for i in range(len(rows)):
        data.append(rows[i][2])
    print('data:',data)

#加總車流量
    sum=0
    for j in range(len(data)):
        sum = int(data[j])+sum
    print(sum)

#將車流量存成陣列
    value.append(sum)
    print(value)
   
    


#錯誤示範    
    """
    for i in range(len(rows)):
        if len(rows[i])<=1:
            data.append(rows[i][2])
        elif len(rows[i])>=2:
            data.append(rows[i][2])
    print(data)
    """