def lower_case(str):
    return str.lower()
inp_str=input("enter number seperate by space :")
str=inp_str.split(" ") #convert the string in to list
list_2=list(map(lower_case,str))
print("cage the value4s into lowercase",list_2)

#convert the str number in to list
'''def add(x):
    return x + 2

user_input = input("Enter numbers separated by space: ")
num_list = list(map(int, user_input.split()))

new_list = list(map(add, num_list))
print("List after adding 2 to each element:", new_list)'''
