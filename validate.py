# validation function
def validate(data,validate_rule):
  k="All"
  result=True
  for key, value in data.items():
      if (validate_rule.get(key, lambda x: False)(value))== False:
        result=False
        k=key
        break
  return k,result


#schema
schema={"name":{"data_type":str,"min":4,"max":10},
        "age":{"data_type":int,"min":16,"max":80},
        "married":{"data_type":bool},
        "address":{"data_type":str,"min":4,"max":20}}

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
      "address":"Bhaktapur"
      }

#testing 
k,result=validate(data,validate_rule)
print(f"{k} Field is {result}")
