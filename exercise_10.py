class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"ID: {self.id}\nName: {self.name}")

employee = Employee(1, "norlyn")
employee.display()

del employee.id

try:
    print(employee.id)
except Exception:
    print("This no longer exist.")

del employee

try:
    print(emplyee)
except Exception:
    print("This object no longer exist.")
