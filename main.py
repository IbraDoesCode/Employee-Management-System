from logo import logo
from functions import *


def main():
    print(logo)

    while True:
        print("Operations: ")
        print("1. Add")
        print("2. View All employees")
        print("3. View employee data")
        print("4. Update Employee data")
        print("5. Delete Employee")
        print("6. Exit")
        print('\n')

        action = input("(1/2/3/4/5/6): ")
        print("\n")
        match action:

            case "1":
                add_employee()
                print("\n")

            case '2':
                view_all_employees()
                print("\n")

            case "3":
                employeeID = int(input("Enter employeeID: "))
                view_employee_details(employeeID)
                print("\n")

            case "4":
                employeeID = int(input("Enter employeeID: "))
                field_name = input("Enter fieldname: ")
                new_data = input("Enter updated info: ")
                update_employee_data(employeeID, field_name, new_data)
                print("\n")

            case "5":
                employeeID = int(input("Enter employeeID: "))
                delete_employee(employeeID)
                print("\n")

            case "6":
                print("Exiting")
                break


main()
