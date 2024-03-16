from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get.all()
    for employee in employees:
     print(employee)
 
    pass


def find_employee_by_name():
 name = input("Enter employee's name: ")
 if employee :=  Employee.find_employee_by_name(name):
    print(employee) if employee else print(
        f"Employee {name} not found."
    )
    pass


def find_employee_by_id():
    id_ = input("Enter the employees id: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(f"Employee with {id_} not found.")

    pass


def create_employee():
    name = input("Enter employee's name: ")
    jobtitle = input("Enter employee's job title: ")
    department = input("Enter employee's department id: ")
    try:
        employee = Employee.create(name, jobtitle, department)
        print(f'succees fully created {name}, {jobtitle}, {department}')
    except Exception as exc:
       print("Invalid entry", exc)

    pass


def update_employee():
    id_=input('Please enter the employee name you want to update: ')
    if employee := Employee.find_by_name(employee):

     try:
         
         name = input("Enter empoyees new: ")
         employee.name = name
         jobtitle = input("Enter employees new job title: ")
         employee.jobtitle = jobtitle
         department = input("Enter employees new deaprtment id: ")
         employee.department = department

         employee.update()
         print(f'succecfully {name} {jobtitle} {department} updated')
     except  Exception as exc:
         print("Error updating employee", exc)

         
         pass


def delete_employee():
 id_ = input("Enter empoyee's id: ")
 if employee := Employee.find_by_id(id_):
     employee.delete()
     print(f"{id} has been deleted.")
 else:
    print(f'empoyee {id} not found')
    pass


def list_department_employees():
    list_department_employees = list_department_employees.get.all()
    for list_department_empoyees in list_department_employees:
        print(list_department_employees)
    pass