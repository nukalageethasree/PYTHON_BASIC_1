import re
string="she sells sea shells on the sea shore"
pattern="sea"
repl="ocean"
new_string=re.sub(pattern,repl,string,1)
print(new_string)