import write
import csv
import numpy as np
import xlwt
from xlwt.Style import add_palette_colour

def XLS():
    with open('pm25.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        column = [row for row in reader]
        #print(column)
        #print(len(column))
        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        f=[]
        g=[]
        h=[]
        k=[] 
        l=[]
        a.append('x')
        b.append('y')
        c.append('AVERAGE CONC')
        d.append('ZELEV')
        e.append('ZHILL')   
        f.append('ZFLAG') 
        g.append('AVE') 
        h.append('GRP')   
        k.append('DATE')
        l.append('NET ID')
        
        
        for i in range(8,len(column)):
            str2 = column[i][0].split()
            #print(str2)
            
            a.append(float(str2[0]))
            b.append(float(str2[1]))
            c.append(float(str2[2]))
            d.append(float(str2[3]))
            e.append(float(str2[4]))
            f.append(float(str2[5]))
            g.append(str2[6])
            h.append(str2[7])
            k.append(float(str2[8]))
            l.append(str2[9])
        
            
    
            workbook = xlwt.Workbook(encoding='utf-8')
            worksheet = workbook.add_sheet('Worksheet')
        #print(len(a))
        for i in range((len(column)-7)):
            #print(i)
            worksheet.write(i, 0,a[i])
            worksheet.write(i, 1,b[i])
            worksheet.write(i, 2,c[i])
            worksheet.write(i, 3,d[i])
            worksheet.write(i, 4,e[i])
            worksheet.write(i, 5,f[i])
            worksheet.write(i, 6,g[i])
            worksheet.write(i, 7,h[i])
            worksheet.write(i, 8,k[i])
            worksheet.write(i, 9,l[i])
        workbook.save('Excel_test.xls') 
        print('Funtion working good')
         
    
    

XLS()