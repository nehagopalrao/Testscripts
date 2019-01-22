def computepay(hrs,rate):
    return

hrs = float(input("Enter Hours:"))
if (hrs <= 0):
    quit()
rate = float(input("Enter rate:"))
if(rate <=0):
    quit()
pay = hrs * rate
if(hrs>0) and (hrs<=40):
    pay = hrs * rate
else:
    hrs_extra = hrs - 40
    extra_pay = float(hrs_extra * 1.5*rate)
    total_pay = extra_pay + (40*rate)

computepay(hrs,rate)
print(total_pay)



#p = computepay(10,20)
#print("Pay",p)
