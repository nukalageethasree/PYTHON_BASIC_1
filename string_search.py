import re
string="she sells sea shells on the sea shore"
pattern="sells"
if re.search(pattern, string):
    print("match found")
else:
    print("pattern not matched")    