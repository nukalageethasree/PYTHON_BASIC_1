stack=[6,9,5,3,4,8]
print("original stack is:",stack)
stack.append(7)
print("stack after pushing the operation:",stack)
stack.pop()
print("stack after poping the operation:",stack)
last_element_index=len(stack)-1
print("value obtaiined after peep operation is:",stack[last_element_index])
max_value=max(stack)
print("max value of the stack",max_value)
stack.sort()
print("sorted value of the stack",stack)
del stack[3]
print("del the number which is present in the index 3:",stack)
