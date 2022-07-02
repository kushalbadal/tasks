# validation function
def validate(dict,validate_rule):
  k="All"
  result="True"
  for key, value in dict.items():
    if (validate_rule.get(key, lambda x: False)(value))== False:
      result="False"
      k=key
      break
  return k,result


dict={"name":"kushal","age":25,"married":False}
validate_rule = {
    "name": lambda x: isinstance(x, str) and 4 <=len(x)<=10,
    "age": lambda x: isinstance(x, int) and 16 <=x <=80,
    "married": lambda x: isinstance(x, bool) ,
}

k,result=validate(dict,validate_rule)
print(f"{k} Field is {result}")
