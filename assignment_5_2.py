largest = None
smallest = None
while True:

    num = input("Enter a number: ")

    if num =="done":
        break
    try:
        x= int(num)
    except:
        print('Invalid input')








    if largest is None or smallest is None:
        largest = x
        smallest = x
    if x > largest:
        largest = x
    if x < smallest:
        smallest = x
    continue

print("Maximum is ", largest)
print("Minimum is", smallest)




    #for smallest in  (num):
    #    smallest = num
    #    if num < smallest:
    #         print('Minimum is ', smallest)

#if num < dmallest:
#    print("Maximum", largest)
