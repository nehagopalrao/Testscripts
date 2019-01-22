hrs = float(input("Enter Hours:"))
#h = float(hrs)
if (hrs<= 0):
    quit()
rate = float(input("Enter hour rate:"))
#r = float(rate)
if(hrs>0) and (hrs<=40):
    pay = hrs * rate
else:
    hrs_extra = hrs - 40
    extra_pay = float(hrs_extra * 1.5*rate)
    total_pay = extra_pay + (40*rate)
print(total_pay)
