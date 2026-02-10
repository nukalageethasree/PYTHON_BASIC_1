states={'delhi':'DL','haryana':'HR','maharastra':'MH','rajasthan':'RJ'}
states['tamil nadu']='TN'
states.setdefault('karnataka','sorry,no idea')
print("code of rajasthanis",states['rajasthan'])
print('-'*5,"codes",'-'*5)
for i in states.items():
    print(i)
print("code of karnataka:",states.get('karnataka'))    