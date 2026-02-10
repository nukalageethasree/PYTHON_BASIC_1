info="for proto.reo@gmail.com sun oct 16 20:29:16 2016"
start = info.find("@")+1
end=info.find(".com")+4
mailserver=info[start:end]
start=end+1
end=len(info)-1
date_time=info[start:end]
print("the email has been sent through"+mailserver)
print("it was sent on "+date_time)