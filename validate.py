# validation function
def validate(dict,int_type,str_type):
    result="True"
    for k in dict:
        if type(dict[k]) == int:
          if k!="name" and k!="Married":
            if dict[k]>int_type["max"] or dict[k]<int_type["min"]:
                result="False"
                break
          else:
            result="False"
            break
        if type(dict[k])==str:
          if k!="age" and k!="Married":
            if len(dict[k])>str_type["max"] or len(dict[k])<str_type["min"]:
                 result="False"
                 break
          else:
            result="False"
            break
        if type(dict[k])==bool:
          if k!="age" and k!="name":
            pass
          else:
            result="False"
            break
    return result


#initialize
dict={"name":"kushal",
      "age":80,
      "Married":True}
str_type={"max":10,
          "min":4}
int_type={"max":80,
          "min":16}
print("Validation:",validate(dict,int_type,str_type))
