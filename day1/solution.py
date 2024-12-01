from collections import Counter


file_path = r"C:\Users\orhun\OneDrive\Documenten\vsc map\adventOfCode2024\day1\input.txt"
with open(file_path, "r") as file:
    data = [list(map(int, line.split())) for line in file]


left, right = zip(*data)

left_sorted = sorted(left)
right_sorted = sorted(right)

part1_total = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
print(f"PART1 solution = {part1_total}")

right_count = Counter(right)
part2_total = sum(l * right_count[l] for l in left)
print(f"SECOND PART BREV {part2_total}")
