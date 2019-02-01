#Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('enter a valid file name:',fname)
    quit()
for line in fh:
    upper_case_text = line.upper()
    delete_extra_line = upper_case_text.rstrip()
    print(delete_extra_line)
