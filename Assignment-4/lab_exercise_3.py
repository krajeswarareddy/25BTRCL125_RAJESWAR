import csv
from pathlib import Path

# Locate employees.csv in the same folder as this script
CSV_FILE = Path(__file__).parent / "employees.csv"
FIELDNAMES = ["emp_id", "name", "department", "basic_salary", "hra", "allowances", "tax_percent"]


def initialize_csv():
    """Creates employees.csv with sample records if it does not exist."""
    if not CSV_FILE.exists():
        sample_employees = [
            {
                "emp_id": "EMP101",
                "name": "Ananya Rao",
                "department": "Engineering",
                "basic_salary": "60000",
                "hra": "18000",
                "allowances": "7000",
                "tax_percent": "10",
            },
            {
                "emp_id": "EMP102",
                "name": "Karthik Reddy",
                "department": "Data Science",
                "basic_salary": "75000",
                "hra": "22500",
                "allowances": "9500",
                "tax_percent": "12",
            },
            {
                "emp_id": "EMP103",
                "name": "Meera Nair",
                "department": "Operations",
                "basic_salary": "48000",
                "hra": "14400",
                "allowances": "5600",
                "tax_percent": "8",
            },
        ]
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(sample_employees)


def calculate_net_salary(row):
    """Computes gross salary, tax deduction, and net salary for an employee row."""
    basic = float(row["basic_salary"])
    hra = float(row["hra"])
    allowances = float(row["allowances"])
    tax_percent = float(row["tax_percent"])

    gross = basic + hra + allowances
    tax_amount = gross * (tax_percent / 100.0)
    net = gross - tax_amount
    return gross, tax_amount, net


def generate_payroll_report():
    """Reads employees.csv and prints a formatted payroll table with totals."""
    print("\n--- CSV Payroll Management Report ---")
    try:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            records = list(reader)

            if not records:
                print("No employee records found in employees.csv.")
                return

            print(
                f"{'ID':<8} {'Name':<16} {'Department':<14} "
                f"{'Gross (INR)':>12} {'Tax (INR)':>11} {'Net Pay (INR)':>14}"
            )
            print("-" * 80)

            total_payroll = 0.0
            for row in records:
                gross, tax_amt, net = calculate_net_salary(row)
                total_payroll += net
                print(
                    f"{row['emp_id']:<8} {row['name']:<16} {row['department']:<14} "
                    f"{gross:>12,.2f} {tax_amt:>11,.2f} {net:>14,.2f}"
                )

            print("-" * 80)
            print(f"{'Total Net Monthly Payroll:':<64} {total_payroll:>14,.2f}")

    except FileNotFoundError:
        print("Error: employees.csv not found.")
    except (ValueError, KeyError) as err:
        print(f"Error parsing CSV data: {err}")


def add_employee():
    """Appends a new employee record to employees.csv."""
    print("\n--- Add New Employee ---")
    try:
        emp_id = input("Enter Employee ID (e.g., EMP104): ").strip()
        name = input("Enter Employee Name: ").strip()
        department = input("Enter Department: ").strip()
        basic = float(input("Enter Basic Salary: ").strip())
        hra = float(input("Enter HRA: ").strip())
        allowances = float(input("Enter Allowances: ").strip())
        tax_percent = float(input("Enter Tax Percentage (e.g., 10): ").strip())

        if not emp_id or not name or not department:
            raise ValueError("Employee ID, Name, and Department cannot be empty.")
        if basic < 0 or hra < 0 or allowances < 0 or not (0 <= tax_percent <= 100):
            raise ValueError("Salary values must be non-negative and tax between 0 and 100.")

        with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writerow(
                {
                    "emp_id": emp_id,
                    "name": name,
                    "department": department,
                    "basic_salary": f"{basic:.2f}",
                    "hra": f"{hra:.2f}",
                    "allowances": f"{allowances:.2f}",
                    "tax_percent": f"{tax_percent:.2f}",
                }
            )
        print(f"Employee '{name}' ({emp_id}) added to employees.csv!")
    except ValueError as err:
        print(f"Invalid input: {err}")
    except OSError as err:
        print(f"File error: {err}")


def main():
    initialize_csv()
    while True:
        print("\n=== CSV-Based Payroll Management System ===")
        print("1. Generate Payroll Report")
        print("2. Add New Employee")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()
        if choice == "1":
            generate_payroll_report()
        elif choice == "2":
            add_employee()
        elif choice == "3":
            print("Exiting Payroll System. All records saved in employees.csv.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()