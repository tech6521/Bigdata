#coding: cp949
my_data=[1,1,1,4,2,44,6,8,6,8]
print(my_data)
unique_data = set(my_data)
print(unique_data)

for i in unique_data:
    print(i)

t_data = (1,4,5,3,77)
for i in t_data:
    print(i)

str_data="Hello world"
for element in str_data:
    print(element)

dic_data = {"이름":"박가은","나이":26,"취미":"수영"}

for element in dic_data:
    print(element)
    
for key in dic_data:
    print(key+' '+str(dic_data[key]))




