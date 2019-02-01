#def Average()
finp = input('enter file name:')

fhand = open(finp)
count = 0
sec_value=0
for line in fhand:
  line = line.rstrip()
  if  not line.startswith('X-DSPAM-Confidence:'):
      continue
  #a=len(line)
  #print(a)
  first_value = line[21:27]
  #float_number = line [23:]
  #print (y)
  sec_value= sec_value+float(first_value)
  count = count + 1
res= sec_value / count
convert_dec_no = round(res,15)
print('Average spam confidence:',convert_dec_no)
