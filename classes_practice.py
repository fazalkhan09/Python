# class investment:
#     def __init__(self,principal,interest,year) -> None:
#         self.p=principal
#         self.i=interest
#         self.n=year
#     def __str__(self) -> str:
#         pass
#     def get_values(self):
#         self.p=int(input("Enter the principal amount : "))
#         self.i=int(input("Enter the interest rate : "))
#         self.n=int(input("Enter the no of years : "))
#     def value_after(self):
#         return self.p(1+self.i)**self



class Investment:
    def __init__(self, principal, interest, years):
        self.principal = principal
        self.interest = interest
        self.years = years

    def __str__(self):
        return f"Principal - ${self.principal:.2f}, Interest rate - {self.interest * 100:.2f}%"

    def value_after(self):
        return self.principal * (1 + self.interest) ** self.years


investment = Investment(1000, 0.055, 5)
print(investment)