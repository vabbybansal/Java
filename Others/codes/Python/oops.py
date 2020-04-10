# Different associations in OOPS
# Inheritance - is a
# Composition - part of
# Aggregation - has a

class EmployeeCalendar(object):
    def __init__(self):
        self.num_leaves = 0

    def addLeaves(self, numDays):
        self.num_leaves += numDays

    def __repr__(self):
        return 'NumLeaves: ' + str(self.num_leaves)

    def __str__(self):
        return 'NumLeaves: ' + str(self.num_leaves)

class EmployeeDepartment(object):
    def __init__(self, department="Unknown"):
        self.department = department

    def __repr__(self):
        return 'Dept: ' + str(self.department)

    def __str__(self):
        return 'Dept: ' + str(self.department)

class Employee(object):

    # strictly class variable
    numOfEmps = 0

    # class variable, but the instances [might] themselves have this variable for personalization
    raiseAmount = 1.4

    # Constructor
    # self refers to the instance
    def __init__(self, first, last, pay, department = None):
        self.first = first
        self.last = last
        self.pay = pay

        # if I do self.numOfEmps, then this will create an instance variable which will override the class variable, which we do not want for numOfEmps as it is strictly class dependent
        Employee.numOfEmps += 1

        # Composition [PART OF: Employee instance gets deleted, the salary instance will also get deleted]
        # ---------------------
        self.calendar = EmployeeCalendar()

        # Aggregation [HAS A: Employee instance gets deleted, department does not get deleted]
        # -------------------
        self.department = department

    def takeLeave(self, numDays):
        self.calendar.addLeaves(numDays)


    # Instance Method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # property Decorator - access functions as if member variables
    # ------------------
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    # property Decorator Setter - access functions as if member variables
    # -------------------------
    @email.setter
    def email(self, email):
        first, last = email.split('.')
        self.first = first
        self.last = last

    # property Decorator Deleter - access functions as if member variables
    # -------------------------
    @email.deleter
    def email(self):
        print 'Deleting email'
        self.first = None
        self.last = None

    def applyRaise(self):
        # self.pay = int(self.pay * Employee.raiseAmount)
        self.pay = int(self.pay * self.raiseAmount)
        # IMPORTANT
        # ---------
        # second statement preffered instead of first as this will allow personalization. If the object instance has raiseAmount, it will override the class variable raiseAmount

    # Class Method
    # ------------
    @classmethod
    def setRaiseAmount(cls, amount):
        cls.raiseAmount = amount

    # Class Methods as alternative constructors
    # -----------------------------------------
    @classmethod
    def objectFromString(cls, empStr):
        first, last, pay = empStr.split('-')
        return cls(first, last, pay) # same as Employee(first, last, pay

    # Static methods - methods which do not use any instance or class methods but are related to the class
    # --------------
    @staticmethod
    def isWorkDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


    # Special Method - repr
    # ---------------------
    # repr - usually a string which is used to reproduce an object | used for logging and debugging
    # If our class does not have a __str__ but has __repr__, then all calls to str fall back to repr
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{}".format(self.fullname())

    def __add__(self, other):
        return "{}, {}".format(self.fullname(), other.fullname())

    def __len__(self):
        return len(self.fullname())


# Inherited Class
# ---------------
class Developer(Employee):

    # Class variable overrides base class variable with the same name, if the scope is the Developer class or Developer class instance
    raiseAmount = 1.8

    # Constructor
    # self refers to the instance
    def __init__(self, first, last, pay, progLang, department=None):
        # Call base class constructor
        # ---------------------------
        super(Developer, self).__init__(first, last, pay, department)
        self.progLang = progLang

# Inherited class
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None, department=None):
        # Call base class constructor
        # ---------------------------
        super(Manager, self).__init__(first, last, pay, department)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def addEmp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def removeEmp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def printEmps(self):
        for emp in self.employees:
            print emp.fullname()
            # print emp.progLang



emp1 = Developer('Vaibhav', 'Bansal', 100, 'C++')
emp2 = Developer('Akku', 'Bansal', 200, 'Python')
emp3 = Manager('Gotaa', 'Bee', 200, [emp1])
# emp3.addEmp(emp1)
emp3.addEmp(emp2)
# emp3.removeEmp(emp1)
print 'Employees under manager'
emp3.printEmps()

# If an object is an instance of a class / base_class
# ---------------------------------------------------
print isinstance(emp3, Manager)  # True
print isinstance(emp3, Employee)  # True
print isinstance(emp3, Developer)  # False

# if a class is a subclass of another class
print issubclass(Manager, Employee)  # True
print issubclass(Manager, object)  # True
print issubclass(Manager, Developer)  # False


print ''
# call special method str / repr overriden in that order
print 'Str / Repr special methods'
print emp3
print str(emp3)
print repr(emp3)
print emp3.__str__()
print emp3.__repr__()

print ''
print 'Add special method add / operator overload'
# call special method add / operator overload
#  ------------------------------------------
print emp1+emp2

print ''
print 'Add special method len / operator overload'
# call special method len / operator overload
#  ------------------------------------------
print len(emp1)


print ''
print 'Property decorator'
# Property Decorator
#  ------------------------------------------
print emp1.email
emp1.email = 'vabby.bansal'
print emp1.fullname()
# Print details about inherited class Developer
print help(Developer)

# Calling method using instance
# -----------------------------
print emp1.fullname()
# Calling method using class
print Employee.fullname(emp1)


# Variable Scope
# --------------
# If both the instance and the class have a variable of the same name, if that variable is called by self, then the object variable is used / overrides the class variable
# So, the variable is first looked within the object, and if not found, is then looked in the class
print ''
# object and class details
print emp1.__dict__
print emp2.__dict__
print Employee.__dict__

print ''
emp1.raiseAmount = 10
print emp1.__dict__
print emp2.__dict__
print Employee.__dict__

print ''
Employee.raiseAmount = 20
print emp1.__dict__
print emp2.__dict__
print Employee.__dict__



# printing strictly class variables
# ---------------------------------
print Employee.numOfEmps

# Invoke class method
# -------------------
Employee.setRaiseAmount(1.3)
print Employee.raiseAmount

# Using class method as alternative constructor
# ---------------------------------------------
Employee.objectFromString('John-Doe-10')

# Static Methods
# --------------
import datetime
print Employee.isWorkDay(datetime.date.today())


# using composition
# -----------------
emp3.takeLeave(3)

# using aggregation
# -----------------
marketingDept = EmployeeDepartment('Marketing')
emp4 = Developer('Vaibhav', 'Gupta', 10, 'Tensor', marketingDept)

print emp1.__dict__
print emp2.__dict__
print emp3.__dict__
print emp4.__dict__
