
# Lab Exercise 1: Log File Reader Program

from pathlib import Path

# Read the log file
file_path = Path(__file__).with_name("sample.log")

try:
    with open(file_path, "r") as file:
        lines = file.readlines()

    print("========== LOG FILE CONTENTS ==========")

    for number, line in enumerate(lines, start=1):
        print(f"{number}. {line.strip()}")

    print("\n========== LOG SUMMARY ==========")
    print("Total Log Entries:", len(lines))
    print("INFO Entries:", sum("INFO" in line for line in lines))
    print("WARNING Entries:", sum("WARNING" in line for line in lines))
    print("ERROR Entries:", sum("ERROR" in line for line in lines))

except FileNotFoundError:
    print("Error: sample.log file not found.")

except Exception as e:
    print("An error occurred:", e)
