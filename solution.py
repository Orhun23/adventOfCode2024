# Define the file path
file_path = r"C:\Users\orhun\OneDrive\Documenten\vsc map\adventOfCode2024\input.txt"

# Initialize a variable to count safe reports
safe_reports = 0

# Read the file and process each row
with open(file_path, "r") as file:
    rows = file.readlines()

# Process each row from the file
for row in rows:
    # Convert the row into a list of integers
    report = list(map(int, row.split()))
    
    # Calculate the differences between consecutive levels
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    # Check if all differences are either positive (increasing) or negative (decreasing)
    is_increasing = all(0 < diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff < 0 for diff in differences)
    
    # If either condition is true, the report is safe
    if is_increasing or is_decreasing:
        safe_reports += 1

# Output the number of safe reports
print(f"Number of safe reports: {safe_reports}")
