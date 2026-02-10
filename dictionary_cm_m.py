m_cm={x:x*100 for x in range(1,11)}
temp=m_cm.values()
cm_m={x:x/100 for x in temp}
print("meters to centimeters:",m_cm)
print("centi meters to meters:",cm_m)