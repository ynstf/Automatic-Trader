import csv
import time
import winsound
import random


x_value = 0
total_1 = 5


prx_dollar=100
ce=100
ib=ce/4
iug=ce/4
se = ib
n=0

t=0
c=0


x_value = 0
frequency = 200  # Set Frequency To 2500 Hertz
duration = 300  # Set Duration To 1000 ms == 1 second
tm = 60
b=0
s=0


fieldnames = ["x_value", "total_1", "ibline", "celine","se"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()


while True:

    s = random.randint(-10,10)
    with open('data.csv', 'a') as csv_file:

        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        x_value += 1
        total_1 = total_1 + s
        info = {
            "x_value": x_value,
            "total_1": total_1,
            "ibline": ib,
            "celine": ib+ce,
            "se":se
            
            
        }

        csv_writer.writerow(info)
        print(x_value, total_1)




    ####################################################

    
    line=ib+(ce/3)
    
    if total_1>ib and t==0:
        #Trade(prx_dollar)
        se = ib
        t = 1
        ib = ib + ib
        
    if total_1>ib+ce and t==1:
        ib = ib + iug
        line = line + iug
        
    if total_1 > line and t==1 and c==0:
        c = 1
        ib= ib+abs(ib/7)

    if total_1<ib and total_1>se and t==1:
        winsound.Beep(frequency, duration)

    if t==0 and abs((ib-total_1)) > ce/2:
        ib=ib-(iug/10.0)
        
    if t==1:
        print ("trade")
        
    if total_1>ib and t==1:
        n=1
        
    if n == 1 and total_1<ib:
        #ClosTrade()
        t=0
        c=0
        n=0
        
    #time.sleep(0.5)
