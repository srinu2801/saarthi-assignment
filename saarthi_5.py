from itertools import permutations

Entities_list=["kolkata", "delhi"]
utterance_list=["How far is <> from <>", "How is the weather in <>"]

out_list = []


for i in range(len(utterance_list)):
    str_i = utterance_list[i]
    n=0
    while "<" in str_i:
        i1=str_i.find("<")
        i2=str_i.find(">")
        
        str_i = str_i[:i1] + "{"+str(n)+"}" + str_i[(i2+1):]
        n+=1
    
    entity = list(permutations(Entities_list,n))
    
    for i in range(len(entity)):
        out_i = str_i.format(*entity[i])
        out_list.append(out_i)

print(out_list)
