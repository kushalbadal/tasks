global searched_data
searched_data={}

def search_sentence(search_term,data_list):
  global searched_data
  temp=[]
  for sentence in data_list:
    if search_term in sentence:
      temp.append(sentence)
  searched_data[search_term]=temp
  return  searched_data[search_term]



data_list=["Trying to make a list","I'll update your address list virtually over the next few years.","It is raining heavily.","There are two people on my list."]


loop= True
while loop:
  search_term = input("enter a word to search")
  if len(search_term.split())==1:
      if search_term in searched_data.keys():
        searched=searched_data[search_term]
      else:
        searched=search_sentence(search_term,data_list)
      print(searched)
  else:
    print("Give a single word for search")

  if input("enter q to continue")!='q':
    loop=False
