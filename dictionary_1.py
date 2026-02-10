'''dict={'roll no':'16/001', 'Name':'NUKALA GEETHA SREE','course':'computer science engineering'}
print(dict)
print("Roll no:",dict['roll no'])
print("name:",dict['Name'])
print("course:",dict['course'])
dict['marks']=95
print("dict[marks]:",dict['marks'])
print(dict)
del dict['course']
print(dict)
dict.clear()
print(dict)
'''
#pop of the dictionary 
dict={'roll no':'16/001', 'Name':'NUKALA GEETHA SREE','course':'computer science engineering'}
print(dict)
print("name is:",dict.pop('Name'))
print("after popping the name :",dict)
print("marks is :",dict.pop('marks',-1))# it will take marks as default
print("dict after poping ths marks:",dict)
print("popping an item random :",dict.popitem())
print(" dict after popping an randon item: ",dict)
