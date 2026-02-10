'''def add(x):
    x+=2
    return x
new_list=list(map(add,range(1,21)))
print(new_list)'''
def add(x):
    x+=2
    return x
list_num=[1,2,3,4,5,6]
print("original list ",list_num)
new_list=list(map(add,list_num))
print("new list after mapping",new_list)

