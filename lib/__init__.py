from helpers import Employee


def list_employees():
    employees = Employee.get_all() 
    for employee in  employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(
        f'employee {name} not found') 


def find_employee_by_id():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(
        f'employee {id_} not found') 


def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter employee's job title: ")
    department_id = input("Enter employees's department id: ")
    try:
        employee = Employee.create(name, job_title, department_id)
        print(f'Success: {employee}')
    except Exception as exc:
        print("Error creating employee: ", exc) 


def update_employee():
    id_ = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(id_):
        try:
            name = input("Enter the employee's new name: ")
            employee.name = name
            job_title = input("Enter employee's new job title: ")
            employee.job_title = job_title
            department_id = input("Enter employees's new department id: ")
            employee.department_id = department_id

            employee.update()
            print(f'Success: {employee}')
        except Exception as exc:
            print("Error updating employee: ", exc)
    else:
        print(f'employee {id_} not found')




def delete_employee():
    id_ = input("Enter the department's id: ")
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f'Employee {id_} deleted')
    else:
        print(f'Employee {id_} not found')


def list_department_employees():
    pass
