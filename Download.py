import csv
from datetime import date
from os import name, write
import requests
import pandas as pd
import io
import time
import Calculation
from apscheduler.schedulers.blocking import BlockingScheduler
import math
import subprocess
import Download_uv
import XLS


def task():
    # 導入套件：day_accumulate ->處理日累積量問題
    
    def timedata_change(result):
        year           = result.tm_year
        month          = result.tm_mon
        day            = result.tm_mday
        hour           = result.tm_hour
        minutes        = result.tm_min
        seconds        = result.tm_sec
        accumulate_day = result.tm_yday
    
        #print(year ,month ,day ,hour ,minutes ,seconds ,accumulate_day)

        
        if (hour<0):
            hour=hour+24
        
        
        if (month<10):
            M = str(month)
            M = '0'+M
            month_txt=str(month)
            month_txt=' '+month_txt
        else:
            M = str(month)
            month_txt=str(month)
        if (day<10):
            D = str(day)
            D = '0'+D
            day_txt=str(day)
            day_txt=' '+str(day)
        else:
            D = str(day)
            day_txt=str(day)
        
        if (hour<10):
            H = str(hour)
            H = '0'+H
            hour_txt=str(hour)
            hour_txt=' '+str(hour)
        else:
            H = str(hour)
            hour_txt=str(hour)
    

        Y    = str(year)
        Hour = str(hour)
        Min  = str(minutes)
        S    = str(seconds)

        TIME= Y+'-'+M+'-'+D+' '+H+':00:00'
        TIME_SFC = Y+'_'+M+'_'+D+'_'+Hour+'_'+Min+'_'+S
        #print(TIME)
        #print(TIME_SFC)
        return TIME
        
    # 抓取資料，下載csv檔
    url = 'https://data.epa.gov.tw/api/v1/aqx_p_142?limit=1000&api_key=93304003-71f2-4da8-8416-64fc1980ef65&sort=ImportDate%20desc&format=csv'
    s=requests.get(url).content
    df_train=pd.read_csv(io.StringIO(s.decode('utf-8')))
    
    
    # 時間
    A=True
    seconds=time.time()
    while(A==True):
        result =time.localtime(seconds)
        timedata_change(result)

        time_condition = len(df_train[(df_train.SiteName=="大里")&(df_train.MonitorDate==timedata_change(result))])
        windspeed_condition = len(df_train[(df_train.SiteName=="大里")&(df_train.ItemId==10)&(df_train.MonitorDate==timedata_change(result))])
        winddirec_condition = len(df_train[(df_train.SiteName=="大里")&(df_train.ItemId==11)&(df_train.MonitorDate==timedata_change(result))])
        ambtemp_condition  = len(df_train[(df_train.SiteName=="大里")&(df_train.ItemId==14)&(df_train.MonitorDate==timedata_change(result))])
        rain_condition = len(df_train[(df_train.SiteName=="大里")&(df_train.ItemId==23)&(df_train.MonitorDate==timedata_change(result))])
        rh_condition = len(df_train[(df_train.SiteName=="大里")&(df_train.ItemId==38)&(df_train.MonitorDate==timedata_change(result))])
        #print(time_condition,windspeed_condition,winddirec_condition,ambtemp_condition,rain_condition,rh_condition)

        List =[time_condition,windspeed_condition,winddirec_condition,ambtemp_condition,rain_condition,rh_condition]
        #print(List)
        A    = 0 in List
        #print(A)
        seconds=seconds-3600
        #print(result)
    
    #print(result)  
    
    year           = result.tm_year
    month          = result.tm_mon
    day            = result.tm_mday
    hour           = result.tm_hour
    minutes        = result.tm_min
    seconds        = result.tm_sec
    accumulate_day = result.tm_yday
    
    print('抓取的資料時間:',year ,month ,day ,hour ,':00')
    
    year_txt=year-2000
    year_txt=str(year_txt)


    if (hour<0):
        hour=hour+24
        
        
    if (month<10):
        M = str(month)
        M = '0'+M
        month_txt=str(month)
        month_txt=' '+month_txt
    else:
        M = str(month)
        month_txt=str(month)
    if (day<10):
        D = str(day)
        D = '0'+D
        day_txt=str(day)
        day_txt=' '+str(day)
    else:
        D = str(day)
        day_txt=str(day)
        
    if (hour<10):
        H = str(hour)
        H = '0'+H
        hour_txt=str(hour)
        hour_txt=' '+str(hour)
    else:
        H = str(hour)
        hour_txt=str(hour)
    

    Y    = str(year)
    Hour = str(hour)
    Min  = str(minutes)
    S    = str(seconds)

    TIME= Y+'-'+M+'-'+D+' '+H+':00:00'
    
    
    
    
    
    # 把抓取的溫度，濕度，雨量，風速，風向資料存在名為data的list中
    data=[]
    # 抓取溫度，濕度，雨量，風速，風向資料的Function
    def download(itemid,name):
        name=df_train[(df_train.SiteName=="大里")&(df_train.ItemId==itemid)&(df_train.MonitorDate==TIME)]
        print(len(name))
                                                                                   

        SiteId=[]
        SiteName=[]
        County=[]
        ItemId=[]
        ItemName=[]
        ItemEngName=[]
        ItemUnit=[]
        MonitorDate=[]
        Concentration=[]
        for i in range(len(name)):
            SiteId.append(name.iloc[i,0])
            SiteName.append(name.iloc[i,1])
            County.append(name.iloc[i,2])
            ItemId.append(name.iloc[i,3])
            ItemName.append(name.iloc[i,4])
            ItemEngName.append(name.iloc[i,5])
            ItemUnit.append(name.iloc[i,6])
            MonitorDate.append(name.iloc[i,7])
            Concentration.append(name.iloc[i,8])
        
        dict={"SiteId":SiteId,"SiteName":SiteName,"County":County,"ItemId":ItemId,"ItemName":ItemName,"ItemEngName":ItemEngName,"ItemUnit":ItemUnit,"MonitorDate":MonitorDate,"Concentration":Concentration}
    
        df=pd.DataFrame(dict)
        df.to_csv('Information.csv',index=False, encoding='big5')

        time.sleep(1)

        file='Information.csv'

        with open(file,encoding='big5') as csvFile:
            csvReader = csv.reader(csvFile)
            datas = list(csvReader)
        
        data.append(datas[1][5])
        data.append(datas[1][8])
        print(data)

        

    # 執行Function

    download(10,'WIND_SPEED')
    download(14,'AMB_TEMP')
    download(11,'WIND_DIREC')
    download(23,'RAINFALL')
    download(38,'RH')

    for j in range(len(data)):
        if data[j]=='x':
            data[j]=0

    #print(data)
    
    

    Uz=float(data[1])
    T=float(data[3])
    RH=float(data[9])
    uv=float(Download_uv.task())
    Pasquill=Calculation.Uv_value(uv,Uz)
    Z=10
    Z0=0.2


    # 計算Td
    Td = Calculation.td(T,RH)

    # 計算混和層高
    mixing_height = Calculation.Mechanical_mixing_height(T,Td,Pasquill,Uz,Z,Z0)


    #print('TD:',Td)
    print('混和層高度：', mixing_height)
    print('uv值',uv)
    print('大氣穩定度',Pasquill)
    

    

    windspeed = float(data[1])
    winddirec = float(data[5])
    ambtemp   = float(data[3])+273
    rainfall  = float(data[7])
    rh        = float(data[9])
    
    
     # 四捨五入或是無條件捨去
    winddirec      = math.floor(winddirec)
    mixing_height  = round(mixing_height)

    print('四捨五入後混合層高度',mixing_height)

    
    # 轉換成str格式
    windspeed        =str(windspeed)
    winddirec        =str(winddirec)
    ambtemp          =str(ambtemp)
    rainfall         =str(rainfall)
    rh               =str(rh)
    accumulate_day   =str(accumulate_day)
    mixing_height    =str(mixing_height)


    
    # 轉換sfc輸入格式
    windspeed       = windspeed+'0'
    winddirec       = winddirec+'.0'
    ambtemp         = str(float(ambtemp)+273)
    rainfall        = rainfall+'0'
    RH_              = rh[:-1]
    mixing_height   = mixing_height+'.'
    temp_pfl        = data[3]+'0'

    
    # 寫入SFC檔
    path='Output.SFC'
    R=open(path,'w')
    R.write('   24.145N  120.684E          UA_ID:   466920  SF_ID:   467490  OS_ID:              VERSION: 21112  BULKRN  CCVR_Sub TEMP_Sub\n')
    R.write(year_txt+'{:>3}'.format(month_txt)+'{:>3}'.format(day_txt)+'{:>4}'.format(accumulate_day)+'{:>3}'.format(hour_txt)+'{:>7}'.format('-4.0')+'{:>7}'.format('0.500')+'{:>7}'.format('-9.000')+'{:>7}'.format('-9.000')+'{:>6}'.format('-999.')+'{:>6}'.format(mixing_height)+'{:>9}'.format('12.3')+'{:>8}'.format('1.2000')+'{:>7}'.format('0.80')+'{:>7}'.format('1.00')+'{:>8}'.format(windspeed)+'{:>7}'.format(winddirec)+'{:>7}'.format('14.0')+'{:>7}'.format(ambtemp)+'{:>7}'.format('2.0')+'{:>6}'.format('0')+'{:>7}'.format(rainfall)+'{:>7}'.format(RH_)+'{:>7}'.format('1010.')+'{:>6}'.format('0')+'{:>15}'.format('NAD-SFC NoSubs'))
    R.close()
    
    # 寫入PFL檔
    path2='Output.PFL'
    R2=open(path2,'w')
    R2.write(year_txt+'{:>3}'.format(month_txt)+'{:>3}'.format(day_txt)+'{:>3}'.format(hour_txt)+'{:>8}'.format('14.0')+'{:>2}'.format('1')+'{:>8}'.format(winddirec)+'{:>9}'.format(windspeed)+'{:>9}'.format(temp_pfl, '.2f')+'{:>9}'.format('99.00')+'{:>9}'.format('99.00'))
    R2.close()

    localtime = time.asctime( time.localtime(time.time()) )
    print ("下載時間:", localtime)   

    #呼叫檔案執行
    path3='aermod.exe'
    subprocess.call(path3)


    #使輸出csv檔案轉檔成xls檔，方便GIS使用
    time.sleep(2)
    XLS.XLS()
    print("轉檔成功")

    time.sleep(10)


    

task()
'''
import open
open.OpenGis()
'''







'''
scheduler=BlockingScheduler()
scheduler.add_job(task,"interval",hours=1)



scheduler.start()
'''

    




