import requests
from bs4 import BeautifulSoup
import csv

# Make a request 
page = requests.get("https://pastebin.com/raw/G0VH1LpS")
soup = BeautifulSoup(page.content, 'html.parser')

#Making txt file and writing content
f = open("unparsed.txt", "w")
f.write(str(soup))
f.close()

count_word=0
count=0
parsed={}
#reading unparsed file
f=open('unparsed.txt','r')   
lines=f.read()
f.close

lines=lines.split('   ')
temp=""
key=[]

#parsing and saving parsed content
f=open('data.csv', 'w')
for line in lines:
  line=line.split("\n")
  for i in line:
    count_word=count_word+1
    if count_word<6:
      if count_word==2:
        temp=temp+i+" "
      elif count_word==4 :
        temp=temp+i+" "
      else:
        temp=temp+i
        key.append(temp)
        f.write("%s," % (temp))
        parsed[temp]=[]
        temp=""

    elif count_word>10:
      if count==0:
        f.write("\n%s," % (i))
      else:
        f.write("%s," % (i))
      parsed[key[count]].append(i)
      count=count+1

    if count==3:
      count=0 


f.close()
print(parsed)
