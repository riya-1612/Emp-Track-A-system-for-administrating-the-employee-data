#CREATNG A CLASS OF EMPLOYEE
class Employee:
    def __init__(self, emp_id, name, age, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def display(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Department: {self.department}, Salary: {self.salary}"

#CREATING DIFFERENT FEATURES OF EMPLOYEE MANAGEMENT SYSTEM
class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, age, department, salary):
        new_employee = Employee(emp_id, name, age, department, salary)
        self.employees.append(new_employee)
        print("Employee added successfully!")

    def view_employees(self):
        if not self.employees:
            print("No employees found.")
        else:
            for emp in self.employees:
                print(emp.display())

    def search_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return emp
        return None

    def update_employee(self, emp_id, name=None, age=None, department=None, salary=None):
        emp = self.search_employee(emp_id)
        if emp:
            if name: emp.name = name
            if age: emp.age = age
            if department: emp.department = department
            if salary: emp.salary = salary
            print("Employee details updated successfully!")
        else:
            print("Employee not found.")

    def delete_employee(self, emp_id):
        emp = self.search_employee(emp_id)
        if emp:
            self.employees.remove(emp)
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

    def save_data(self, filename="employee_data.txt"):
        with open(filename, "w") as file:
            for emp in self.employees:
                file.write(f"{emp.emp_id},{emp.name},{emp.age},{emp.department},{emp.salary}\n")
        print("Data saved successfully!")

    def load_data(self, filename="employee_data.txt"):
        try:
            with open(filename, "r") as file:
                self.employees = []
                for line in file:
                    emp_id, name, age, department, salary = line.strip().split(',')
                    self.add_employee(emp_id, name, int(age), department, float(salary))
            print("Data loaded successfully!")
        except FileNotFoundError:
            print("No saved data found.")


#CREATING A MAIN FUNCTION WHICH WILL EXECUTE

def main():
    system = EmployeeManagementSystem()
    system.load_data()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Save Data")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            age = int(input("Enter Employee Age: "))
            department = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            system.add_employee(emp_id, name, age, department, salary)

        elif choice == '2':
            system.view_employees()

        elif choice == '3':
            emp_id = input("Enter Employee ID to search: ")
            emp = system.search_employee(emp_id)
            if emp:
                print(emp.display())
            else:
                print("Employee not found.")

        elif choice == '4':
            emp_id = input("Enter Employee ID to update: ")
            name = input("Enter new name (or press Enter to skip): ")
            age = input("Enter new age (or press Enter to skip): ")
            department = input("Enter new department (or press Enter to skip): ")
            salary = input("Enter new salary (or press Enter to skip): ")

            system.update_employee(emp_id,
                                   name=name if name else None,
                                   age=int(age) if age else None,
                                   department=department if department else None,
                                   salary=float(salary) if salary else None)

        elif choice == '5':
            emp_id = input("Enter Employee ID to delete: ")
            system.delete_employee(emp_id)

        elif choice == '6':
            system.save_data()

        elif choice == '7':
            system.save_data()
            print("Exiting the system")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
