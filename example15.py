# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
user_input=input('Enter a digit')
n1=int("%s"%(user_input) )
n2=int("%s%s"%(user_input,user_input))
n3=int("%s%s%s"%(user_input,user_input,user_input))
n4=int("%s%s%s%s"%(user_input,user_input,user_input,user_input))
n=n1+n2+n3+n4
print("Result : ",n)