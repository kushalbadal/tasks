#search function
def search_sentence(search_term,data_list):
  searched_data=[]
  for sentence in data_list:
    if search_term in sentence:
      searched_data.append(sentence)

  return searched_data


#data
data_list=["Trying to make a list","I'll update your address list virtually over the next few years.","It is raining heavily.","There are two people on my list."]
search_term = "list"

#check the search word
if len(search_term.split())==1:
  searched_data=search_sentence(search_term,data_list)
  print(searched_data)
else:
  print("Give a single word for search")
