# Define the file path
file_path = r"C:\Users\orhun\OneDrive\Documenten\vsc map\adventOfCode2024\input.txt"

fixable_reports = 0
with open(file_path, "r") as file:
    rows = file.readlines()

for row in rows:
    report = list(map(int, row.split()))
    
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    is_increasing = all(0 < diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff < 0 for diff in differences)
    
    if is_increasing or is_decreasing:
        fixable_reports += 1
    else:
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]
            
            modified_differences = [modified_report[j + 1] - modified_report[j] for j in range(len(modified_report) - 1)]
            
            is_increasing = all(0 < diff <= 3 for diff in modified_differences)
            is_decreasing = all(-3 <= diff < 0 for diff in modified_differences)
            
            if is_increasing or is_decreasing:
                fixable_reports += 1
                break

# Output the total number of rows that are safe or fixable
print(f"Number of safe or fixable reports: {fixable_reports}")
