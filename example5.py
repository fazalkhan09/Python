# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
class String_Manupulation(object):
    def __init__(self):
        self.s=""
    def getString(self):
        self.s=input("Enter a string")
    def printing_string(self):
        print(self.s.upper())
def testing_String_Manupulation():
    obj=String_Manupulation()
    obj.getString()
    obj.printing_string()
if __name__== "__main__":
    testing_String_Manupulation()