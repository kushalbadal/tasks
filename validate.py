# validation function
def validate(data,validate_rule):
  k="All"
  result=True
  
  #validation
  for key, value in schema.items():
    #validate only keys present in schemas and required
    if value["required"]==True:
      if key in data.keys():
        if (validate_rule.get(key, lambda x: False)(data[key]))== False:
          result=False
          k=key
          break
      else:
        return key,"required"

    #validate not required field
    else:
      if key in data.keys():
        if (validate_rule.get(key, lambda x: False)(data[key]))== False:
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
      "group":"yellow",
      "country":"Nepal"
      }

#testing 
k,result=validate(data,validate_rule)
print(f"{k} Field is {result}")
