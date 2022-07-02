# validation function
def validate(data,validate_rule):
  k="All"
  result=True
  search_required=[i for i,v in schema.items() if v["required"]==True]
  
  #validate required
  for search in search_required:
    if search in data.keys():
      pass
    else:
      return search,"required"

  #validate rule
  for key, value in data.items():
    #validate fields present in schemas otherwise leave as it is
    if key in schema.keys():
      if (validate_rule.get(key, lambda x: False)(value))== False:
        result=False
        k=key
        break
  return k,result


#schema
schema={"name":{"data_type":str,"min":4,"max":10,"required":True},
        "age":{"data_type":int,"min":16,"max":80,"required":True},
        "married":{"data_type":bool,"required":False},
        "address":{"data_type":str,"min":4,"max":20,"required":False}}

#Making Validation Rule
validate_rule={}
for key,v in schema.items():
  #String_type
  if v["data_type"]==str:
    validate_rule[key]= lambda x: isinstance(x,str) and v["min"] <=len(x)<= v["max"]
  
  #Integer_type
  if v["data_type"]==int:
    min=v["min"]
    max=v["max"]
    validate_rule[key]= lambda x: isinstance(x,int) and min <= x <= max  

  #Boolean_type
  if v["data_type"]==bool:
    validate_rule[key]= lambda x: isinstance(x,bool)


#defining_data
data={"name":"kushal",
      "age":22,
      "married":True,
      "address":"Bhaktapur",
      "group": "yellow"
      }

#testing 
k,result=validate(data,validate_rule)
print(f"{k} Field is {result}")
