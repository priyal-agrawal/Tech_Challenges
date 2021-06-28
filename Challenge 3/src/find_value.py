## editor : Priyal Agrawal
## Function find_value takes the user inputed nested object(dict) and key to find the values

def find_value(obj,key,val=None):
    
    if val is None:
        val=[]
    if obj.get(key):
        val.append(obj.get(key))
        obj.pop(key)
    else:
        for i,j in obj.items():
            if isinstance(obj[i],list):
                find_value(obj[i][0],key,val)
            elif isinstance(obj[i],dict):
                find_value(obj[i],key,val)
    return val

if __name__ == '__main__':
    d = input('Enter dictionary separated by ":" ')
    obj = eval(d)
    key = input('Enter key to search ') 
    print(find_value(obj,key)
