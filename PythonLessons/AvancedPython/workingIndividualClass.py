class Employee:
    # common class base for all employees
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ",self.name, ", Salary: ", self.salary)

# This is going to create first object of our employee class


emp1 = Employee ("Greg", 5000)
emp2 = Employee ("Chris", 7000)
emp1.displayEmployee()
emp2.displayEmployee()
