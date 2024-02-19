# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
total_amount=0
while True:
    user_input=input("Enter the amount to deposite and withdraw")
    if not user_input:
        break
    try:
        values=user_input.split(" ")
        operations=values[0]
        amount=int(values[1])
        if operations=="D":
            total_amount+=amount
        elif operations=="W":
            total_amount-=amount
        else:
            pass
    except ValueError:
        print("Invalid Input. Please enter a valid operation as \'D amount\' and \'W amount\' ")
print("Total amount : " + total_amount)