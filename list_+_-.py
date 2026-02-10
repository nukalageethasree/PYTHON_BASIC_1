def positive(x):
    if x>=0:
        return x
def negative(x):
    if x<0:
        return x
    
positive_num=list(filter(positive,range(-10,30)))
print("positive numbr from the list",positive_num)
negative_num=list(filter(negative,range(-20,30)))
print("negative numbers from the list",negative_num)


