import numpy as np
import pandas as pd
import re
import xlsxwriter

dosya=pd.read_excel("kulucka2_ogrenci_listesi.xlsx")


parts=re.split('[$,_\[\]]',str(dosya)) #Aranılan desen string içerisinde bulunduğu durumda, eşleştiği bölgelerden string’i böler ve bölünmüş halini liste olarak getirir. Herhangi bir eşleşme olmadığı durumda stringin kendisini getirir.
#parts=re.split('[\W\_]',str(dosya)) çok fazla listeyi karıştırıyor istenilen elemanları bununla çıkaramadım

parts=[val for val in parts if val]

parts.pop()

data1=[parts[1],parts[6],parts[11],parts[16]]
data2=[parts[2],parts[7],parts[12],parts[17]]
data3=[parts[3],parts[8],parts[13],parts[18]]
data4=[parts[4],parts[9],parts[14],parts[19]]
data5=[parts[5],parts[10],parts[15],parts[20]]

col1="ID"
col2="İsim"
col3="Soyisim"
col4="Bölüm" 
col5="Sınıf"

df=pd.DataFrame({col1:data1,col2:data2,col3:data3,col4:data4,col5:data5})
df= df.to_string(index=False)


workbook = xlsxwriter.Workbook('kulucka2_yeni_ogrenci_listesi.xlsx')
 
worksheet = workbook.add_worksheet()
 
worksheet.write("A1",col1)
worksheet.write("A2",data1[0])
worksheet.write("A3",data1[1])
worksheet.write("A4",data1[2])
worksheet.write("A5",data1[3])

worksheet.write("B1",col2)
worksheet.write("B2",data2[0])
worksheet.write("B3",data2[1])
worksheet.write("B4",data2[2])
worksheet.write("B5",data2[3])

worksheet.write("C1",col3)
worksheet.write("C2",data3[0])
worksheet.write("C3",data3[1])
worksheet.write("C4",data3[2])
worksheet.write("C5",data3[3])

worksheet.write("D1",col4)
worksheet.write("D2",data4[0])
worksheet.write("D3",data4[1])
worksheet.write("D4",data4[2])
worksheet.write("D5",data4[3])

worksheet.write("G1",col5)
worksheet.write("G2",data5[0])
worksheet.write("G3",data5[1])
worksheet.write("G4",data5[2])
worksheet.write("G5",data5[3])
workbook.close()

