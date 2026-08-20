# Input: number of laps
n = int(input("Enter number of laps: "))

# -------------------------------
# Formula-based solution (O(1))
# -------------------------------
total_points_formula = n * (n + 1) // 2
print("Formula solution:", total_points_formula)

# -------------------------------
# Loop-based solution (O(n))
# -------------------------------
total_points_loop = 0
for i in range(1, n + 1):
    total_points_loop += i
print("Loop solution:", total_points_loop)

# -------------------------------
# Nested loop solution (O(n^2))
# -------------------------------
total_points_nested = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        total_points_nested += 1
print("Nested loop solution:", total_points_nested)
