class employee:
    def __init__(self,name,age,salary,dept) -> None:   
        self.E_name=name
        self.E_age=age
        self.E_salary=salary
        self.E_dept=dept
    def __str__(self) -> str:
        return 
    def display(self):
        print("Emloyee Name: " + self.E_name)
        print("Emloyee Age: " + str(self.E_age))
        print("Emloyee Salary: " + str(self.E_salary))
        print("Emloyee Dept: " + self.E_dept)
emp=employee("Shadman",22,21000.00,"Store keepers")   
emp.display()     