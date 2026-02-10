import re
string="she sells sea shells in the sea "
pattern="shells"
if re.match(pattern, string):
    print("pattern match")
else:
    print("pattern is not there in the string")
pattern_2="she"
if re.match(pattern_2,string):
            print("pattern match")
else:
      print("pattern is not there in the string")              