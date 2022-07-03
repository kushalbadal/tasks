
data1={"District":["kathmandu","Kavrepalanchowk","Dhanusha"],
       "KPI_1":[0.8,0.75,0.85]}

data2={"District":["kathmandu","Kavrepalanchowk","Dhanusha"],
       "KPI_2":[0.35,0.65,0.6]}


coln=[]
merged_data=data1
for i in data2.keys():
    if i in data1.keys():
      pass
    else:
      coln.append(i)
    pass

for key in coln:
  merged_data[key]=data2[key]

  
print(merged_data)
