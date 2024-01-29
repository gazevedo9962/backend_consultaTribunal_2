import sys

string = ""
for value in sys.argv:
    print(value)
    string = string + " " + value

#text = string.split(["-p", " "])
def cat_string_list(list):
    string = ""
    for value in list:
        string = string + " " + value    
    return string    

def cat_arg(parametro, string_arg):
    array_string = string_arg.split()
    for s in array_string:
        if [ s == parametro ]:
            path = array_string[ array_string.index(parametro) + 1 ]
    return path                    

q, p = cat_arg("-q", string), cat_arg("-p", string)
print(f"-q : {q}")
print(f"-p : {p}")
   