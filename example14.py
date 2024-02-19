# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
sentence= input('Enter a sentene : ')
dic={'UPPER':0,'lower':0}
for i in sentence:
    if i.isupper():
        dic['UPPER']+=1
    elif i.islower():
        dic['lower']+=1
    else:
        pass
print('Upper letters in Number : ',dic['UPPER'])
print('Lower letters in Number : ',dic['lower'])