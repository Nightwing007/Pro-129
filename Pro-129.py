import csv
import pandas as pd

csv1 = 'bright_stars.csv'
csv2 = 'unit_converted_stars.csv'

dataset1 = []
dataset2 = []
with open(csv1,'r',encoding='utf8') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        dataset1.append(i)
        
with open(csv2,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        dataset2.append(i)

header1 = dataset1[0]
header2 = dataset2[0]

p_dataset1 = dataset1[1:]
p_dataset2 = dataset2[1:]

h = header1+header2

p_d =[]

for i in p_dataset1:
    p_d.append(i)
for j in p_dataset2:
    p_d.append(j)
with open("total_stars.csv",'w',encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(p_d)
    
df = pd.read_csv('total_stars.csv')
df.tail(8)