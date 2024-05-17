import csv


def retrieve_data():
    data = []
    try:
        with open('Employee Data.csv', 'r') as employeeData:
            reader = csv.DictReader(employeeData)
            for line in reader:
                data.append(line)
    except FileNotFoundError as e:
        print(e)
        return None
    return data


# Create
def add_employee():
    try:
        with open('Employee Data.csv', 'r') as employeeData:
            reader = csv.DictReader(employeeData)
            headers = reader.fieldnames

        employee_data = {}
        for header in headers:
            if header == "Gross Semi-monthly Rate" or header == "Hourly Rate":
                continue
            elif header == "Birthday":
                data = input(f"{header}(DD/MM/YYYY): ")
            else:
                data = input(f"{header}: ")
            employee_data[header] = data

        with open('Employee Data.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=headers)

            writer.writerow(employee_data)
            print("Employee added successfully")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(e)

# Read
def view_all_employees():
    data = retrieve_data()

    print(f"{'Employee ID':20} {'Employee Name':<30} {'Position':<30} {'Basic Salary':30}")
    for line in data:
        emp_id = line['Employee #']
        name = f"{line['First Name'].strip()} {line['Last Name']}"
        basic_salary = line['Basic Salary']
        position = line['Position']
        print(f"{emp_id:20} {name:<30} {position:<30} {basic_salary:<30}")


def view_employee_details(employee_no: int):
    employee_data = retrieve_data()
    found = False
    for data in employee_data:
        try:
            employee_id = int(data['Employee #'])
            if employee_no == employee_id:
                headers = employee_data[0].keys()
                for header in headers:
                    value = data.get(header)
                    print(f"{header}: {value}")
                found = True
                break

        except ValueError:
            pass

    if not found:
        print("Invalid Employee No.")


# Update
def update_employee_data(employee_no, header: str, new_data: str):
    try:
        employee_data = retrieve_data()
        updated = False

        for data in employee_data:
            if data['Employee #'] == str(employee_no):
                data[header] = new_data
                updated = True
                break

        if updated:
            with open('Employee Data.csv', 'w', newline='') as file:
                csvWriter = csv.DictWriter(file, fieldnames=employee_data[0].keys())

                csvWriter.writeheader()
                csvWriter.writerows(employee_data)
            print("Employee Data updated successfully")
        else:
            print("Data record was not found")

    except Exception as e:
        print("An error occurred", e)


# Delete
def delete_employee(employee_no: int):
    employee_data = retrieve_data()
    removed = False
    updated_data = []
    try:
        for data in employee_data:
            if data['Employee #'] == str(employee_no):
                removed = True
                break
            else:
                updated_data.append(data)

        if removed:
            with open('Employee Data.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=employee_data[0].keys())
                writer.writeheader()
                writer.writerows(updated_data)
            print("Employee data deleted successfully")
        else:
            print("Employee ID# not found")

    except Exception as e:
        print("An Error Occurred", e)