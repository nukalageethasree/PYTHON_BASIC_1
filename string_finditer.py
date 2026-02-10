import re
pattern=r"[a-zA-Z]+ \d+"
string="LXI 2013,VXI 2015,VDI 2015,VDI 20104,Maruti suzuki cars in india"
matches=re.finditer(pattern , string)
for match in matches:
    print("found at the index:",match.start())
    print("end at the index:",match.end())
    print("found at the index and end at which index:",match.span())
    
    
