# Employee-Management-System
This Python console based program provides functionalities for managing employee data including adding, viewing, updating, and deleting employee records from a csv file.


This Python program provides functionalities for managing employee data including adding, viewing, updating, and deleting employee records.

Features
Add Employee: Allows users to add a new employee to the system by providing necessary details such as employee ID, name, contact information, salary, etc.
View All Employees: Displays a list of all employees along with their basic details such as employee ID, name, position, and basic salary.
View Employee Details: Enables users to view detailed information about a specific employee by entering their employee ID.
Update Employee Data: Allows users to update the information of an existing employee by specifying the employee ID, the field to be updated, and the new data.
Delete Employee: Provides functionality to remove an employee from the system based on their employee ID.
Usage
Adding Employee:

Run the add_employee() function.
Enter the required details for the new employee as prompted.
Viewing All Employees:

Run the view_all_employees() function.
Viewing Employee Details:

Run the view_employee_details(employee_no) function, providing the employee ID as an argument.
Updating Employee Data:

Run the update_employee_data(employee_no, header, new_data) function, providing the employee ID, the field to be updated, and the new data.
Deleting Employee:

Run the delete_employee(employee_no) function, providing the employee ID of the employee to be deleted.
Data Storage
Employee data is stored in a CSV file named MotorPH Employee Data.csv. This file contains columns corresponding to different employee attributes such as employee ID, name, position, salary, etc.

Dependencies
Python 3.x
csv module
Note
Ensure that the CSV file (MotorPH Employee Data.csv) exists in the same directory as the program file.
