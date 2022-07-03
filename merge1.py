from difflib import SequenceMatcher
import pandas as pd

data1={"District":["kathmandu","Kavre palanchowk","Dhanusa"],
       "KPI_1":[.8,.75,.85]}

data2={"District":["kathmandu","Kavrepalanchowk","Dhanusha"],
       "KPI_2":[.35,.65,.6]}

#check for same data
count1=0
count2=0
for i in data2["District"]:
  for j in data1["District"]:
    if (SequenceMatcher(None, i,j ).ratio())>0.9:
      data1["District"][count2]=data2["District"][count1]
    count2=count2+1
  count2=0
  count1=count1+1


df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)


data1=df1.merge(df2,how='inner')
print(data1)
