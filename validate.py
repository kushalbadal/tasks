#validation Function
def validate(data,validate_rule):
  k="All"
  result=True
  for key, value in data.items():
    for i in value["value"]:
      if (validate_rule.get(key, lambda x: False)(i))== False:
        result=False
        k=key
        break
  return k,result


#data
data={"name":{"id":1, "value":["kushal","Nabin"],"data_type":str},
      "age":{"id":2,"value":[24,28,34],"data_type":int},
      "married":{"id":3,"value":[True],"data_type":bool},
      "address":{"id":4,"value":["bhaktapur"],"data_type":str}
      }

#Defining Rule
rule={"id":{1:{"min":4,"max":20},
            2:{"min":16,"max":80},
            4:{"min":5,"max":20}}}


#Making Validation Rule
validate_rule={}
for key,v in data.items():
  id_value=v["id"]
  #String_type
  if v["data_type"]==str:
    validate_rule[key]= lambda x: isinstance(x,str) and rule["id"][id_value]["min"] <=len(x)<= rule["id"][id_value]["max"]
  
  #Integer_type
  if v["data_type"]==int:
    min=rule["id"][id_value]["min"]
    max=rule["id"][id_value]["max"]
    validate_rule[key]= lambda x: isinstance(x,int) and min <= x <= max  

  #Boolean_type
  if v["data_type"]==bool:
    validate_rule[key]= lambda x: isinstance(x,bool)


k,result=validate(data,validate_rule)
print(f"{k} Field is {result}")

