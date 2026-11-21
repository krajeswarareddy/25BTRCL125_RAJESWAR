from pathlib import Path

# Locate student_data.txt in the same folder as this script
DATA_FILE = Path(__file__).parent / "student_data.txt"


def initialize_sample_data():
    """Creates the file with initial student records if it does not exist."""
    if not DATA_FILE.exists():
        initial_records = [
            "25BTRCL101,Aarav Sharma,CSE-AIML,88.5\n",
            "25BTRCL102,Diya Nair,CSE-AIML,92.0\n",
            "25BTRCL103,Rohan Verma,CSE-AIML,79.5\n",
        ]
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            file.writelines(initial_records)


def view_students():
    """Reads and displays all student records from the file."""
    print("\n--- Student Records ---")
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file if line.strip()]
            if not lines:
                print("No student records found.")
                return
            print(f"{'Roll No':<14} {'Name':<18} {'Branch':<12} {'Marks':<6}")
            print("-" * 52)
            for line in lines:
                roll_no, name, branch, marks = line.split(",")
                print(f"{roll_no:<14} {name:<18} {branch:<12} {marks:<6}")
    except FileNotFoundError:
        print("Error: student_data.txt not found.")
    except ValueError:
        print("Error: Corrupted record format in student_data.txt.")


def add_student():
    """Appends a new student record to the file with input validation."""
    print("\n--- Add New Student ---")
    try:
        roll_no = input("Enter Roll Number (e.g., 25BTRCL125): ").strip()
        name = input("Enter Student Name: ").strip()
        branch = input("Enter Branch (e.g., CSE-AIML): ").strip()
        marks_input = input("Enter Marks (0-100): ").strip()

        if not roll_no or not name or not branch:
            raise ValueError("Roll number, name, and branch cannot be empty.")

        marks = float(marks_input)
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100.")

        with open(DATA_FILE, "a", encoding="utf-8") as file:
            file.write(f"{roll_no},{name},{branch},{marks}\n")

        print(f"Student '{name}' added successfully!")
    except ValueError as err:
        print(f"Invalid input: {err}")
    except OSError as err:
        print(f"File error: {err}")


def search_student():
    """Searches for a student record by Roll Number."""
    print("\n--- Search Student ---")
    target_roll = input("Enter Roll Number to search: ").strip().lower()
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue
                roll_no, name, branch, marks = line.strip().split(",")
                if roll_no.lower() == target_roll:
                    print(f"Found -> Roll No: {roll_no} | Name: {name} | Branch: {branch} | Marks: {marks}")
                    return
        print("Student record not found.")
    except FileNotFoundError:
        print("Error: student_data.txt not found.")


def main():
    initialize_sample_data()
    while True:
        print("\n=== Student Data Manager ===")
        print("1. View All Students")
        print("2. Add Student Record")
        print("3. Search Student by Roll No")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            view_students()
        elif choice == "2":
            add_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting Student Data Manager. Data saved to student_data.txt.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()