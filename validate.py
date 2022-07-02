# validation function
def validate(dict,validate_rule):
  k="All"
  result=True
  for key, value in dict.items():
    for i in value["value"]:
      if (validate_rule.get(key, lambda x: False)(i))== False:
        result=False
        k=key
        break
  return k,result


dict={"name":{"value":["kushal","Nabin"],"data_type":str,"min_length":4,"max_length":10},
      "age":{"value":[25,28,34],"data_type":int,"min_value":16,"max_value":80},
      "married":{"value":[True],"data_type":bool},
      "address":{"value":["bhaktapur"],"data_type":str,"min_length":4,"max_length":15}
      }


validate_rule={}
for key,v in dict.items():
 
  if v["data_type"]==str:
    validate_rule[key]= lambda x: isinstance(x,str) and v["min_length"] <=len(x)<=v["max_length"]
  
  if v["data_type"]==int:
    min=v["min_value"]
    max=v["max_value"]
    validate_rule[key]= lambda x: isinstance(x,int) and min <= x <= max
  

  if v["data_type"]==bool:
    validate_rule[key]= lambda x: isinstance(x,bool)


k,result=validate(dict,validate_rule)
print(f"{k} Field is {result}")
