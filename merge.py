
import pandas as pd

#reading file
f=open('data.txt','r')   
lines=f.readlines()
f.close

count=0
count_index=0
data=[]
temp={}
key=[]
temp_data=[]

#parsing Data
for line in lines:
  line=line.split('|')
  for i in line:
    if count_index>1:
      count_index=0
    if i!='\n':
      i=i.replace("\n","")
      i=i.replace(" ","")
      if count==0:
        key.append(i)
        temp[i]=[]
      else:
        temp[key[count_index]].append(i)
        count_index=count_index+1
    else:
      data.append(temp)
      temp={}
      key=[]
      count=-1

  count=count+1

#parsing for last data
data.append(temp)
df=pd.merge(pd.DataFrame(data[0]),pd.DataFrame(data[1]))
for i in range(2,len(data)):
  df = pd.merge(pd.DataFrame(data[i]),df)
  
print(df)
