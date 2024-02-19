# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
sentence=input('Enter a sentence : ')
dic={'Digits':0,'Words':0}
for i in sentence:
    if i.isdigit():
        dic['Digits']+=1
    elif i.isalpha():
        dic['Words']+=1
    else:
        pass
print('Letters are : ',dic['Words'])
print('DIGITS is : ',dic['Digits'])