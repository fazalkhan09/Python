def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
num=eval(input('Enter the number to find out its factorial'))
print(fact(num))