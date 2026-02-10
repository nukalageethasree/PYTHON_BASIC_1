import re
pattern=r"[a-zA-Z]+ \d+"
string="LXI 2013,VXI 2015,VDI 2015,VDI 20104,Maruti suzuki cars in india"
matches=re.findall(pattern , string)
print(matches)