# validation function
def validate(dict,int_type,str_type):
    result="True"
    for k in dict:
        if type(k) == int:
              if k>int_type["max"] or k<int_type["min"]:
                result="False"
                break
        if type(k)== str:
              if len(k)>str_type["max"] or len(k)<str_type["min"]:
                result="False"
                break
        if type(k) == bool:
          pass
        if type(dict[k]) == str:
              if len(dict[k])>str_type["max"] or len(dict[k])<str_type["min"]:
                result="False"
                break

        if type(dict[k]) == int:
              if dict[k]>int_type["max"] or dict[k]<int_type["min"]:
                result="False"
                break

        if type(dict[k])==bool:
                  pass
    return result


#initialize
dict={20:24,"name":"kushal","married":False}
print(dict)
str_type={"max":10,
          "min":4}
int_type={"max":80,
          "min":16}
print("Validation key and value:",validate(dict,int_type,str_type))

#validating value
def validate(dict,int_type,str_type):
    result="True"
    for k in dict:
        if type(k) == int:
            if type(dict[k]) == int:
              if dict[k]>int_type["max"] or dict[k]<int_type["min"]:
                result="False"
                break
            else:
              if type(dict[k])==bool:
                pass
              else:
                result="False"
                break
        if type(k)== str:
            if type(dict[k]) == str:
              if len(dict[k])>str_type["max"] or len(dict[k])<str_type["min"]:
                result="False"
                break
            else:
              if type(dict[k])==bool:
                pass
              else:
                result="False"
                break
    return result

dict={20:24,"name":"kushal","married":True}
print(dict)
str_type={"max":10,
          "min":4}
int_type={"max":80,
          "min":16}
print("Validation value only:",validate(dict,int_type,str_type))
